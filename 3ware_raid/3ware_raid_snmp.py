#!/usr/bin/env python

# Very quick hack to monitor 3ware RAID cards via SNMP with check_mk
# Tested using Windows 3ware SNMP plugin (3wSnmp.msi from http://kb.lsi.com)
# Hereward Cooper <coops@fawk.eu> - Sep 2012

# MIB: TW-RAID-MIB
# .1.3.6.1.4.1.1458.100.22.1.10.X = twRaidDriveStatus.X
# 255 = OK


def inventory_3ware_raid_snmp(checkname, info):
    inventory = []
    # If 'info' isn't empty, add it to the inventory
    if info != []:
            inventory.append( (None, None) )
    return inventory


def check_3ware_raid_snmp(item, params, info):

    output = ""
    retval = 0

    # Check the results and return appropriately
    for count, rawcheck in enumerate(info):
        check = rawcheck[0]
        if check == '0':
            output += "Array %s OK, " % (count)
        else:
            output += "Array %s Error (code: %s), " % (count, check)
            retval = 2

    if retval == 0:
            output = "OK - " + output[:-2]
    elif retval == 2:
            output = "CRITICAL - " + output[:-2]
    return (retval, output)


check_info["3ware_raid_snmp"] = (check_3ware_raid_snmp, "3ware RAID Arrays", 0, inventory_3ware_raid_snmp)
snmp_info["3ware_raid_snmp"] = ( ".1.3.6.1.4.1.1458.100.23.1", ["7"] )
