#! /bin/bash

adb shell "echo 8 > /proc/sys/kernel/printk"

adb shell "echo 0 > /proc/sys/kernel/panic"

adb shell "echo 1 > /sys/devices/platform/soc/5c00000.qcom,ssc/subsys7/keep_alive"

adb shell "echo 0 >/sys/devices/system/cpu/cpu1/online"

adb shell "echo 0 >/sys/devices/system/cpu/cpu2/online"

adb shell "echo 0 >/sys/devices/system/cpu/cpu3/online"

adb shell "echo 0 >/sys/devices/system/cpu/cpu4/online"

adb shell "echo 0 >/sys/devices/system/cpu/cpu5/online"

adb shell "echo 0 >/sys/devices/system/cpu/cpu6/online"

adb shell "echo 0 >/sys/devices/system/cpu/cpu7/online"

adb shell "echo c >/proc/sysrq-trigger"

#exit 0


