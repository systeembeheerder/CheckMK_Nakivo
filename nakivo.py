#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
#
# Syteembeheerder 2023-04-13
#
#
#<<<nakivo:sep(124)>>>
#253|Cluster1|Scheduled|Failed (180 VM successful, 1 VM failed, 0 VM stopped)
#254|Cluster2|Scheduled|Successful

from .agent_based_api.v1 import *

def discover_nakivo(section):
    for _id, job, _start, _status in section:
        yield Service(item=job)

def check_nakivo(item, section):
    for id_, job, _start, status in section:
        if job == item:
            if status.split()[0] == "Successful":
                yield Result(state=State.OK, summary=status)
            else:
                yield Result(state=State.WARN, summary=status)
            return

register.check_plugin(
    name="nakivo",
    service_name="Nakivo %s",
    discovery_function=discover_nakivo,
    check_function=check_nakivo,
)
