# Copyright (C) 2012 The Android Open Source Project
# Copyright (C) 2015-2017 The JDCTeam
# Copyright (C) 2017 The LineageOS Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
#
# This leverages the loki_patch utility created by djrbliss which allows us
# to bypass the bootloader checks on jfltevzw and jflteatt
# See here for more information on loki: https://github.com/djrbliss/loki
#

"""Custom OTA commands for jf devices"""

def FullOTA_InstallEnd(info):
  info.script.Mount("/system")
  info.script.AppendExtra('ifelse(is_substring("I337", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /system/rild/gsm/* /system/ && busybox rm /system/lib/libcnefeatureconfig.so"));')
  info.script.AppendExtra('ifelse(is_substring("I545", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /system/rild/vzw/* /system/"));')
  info.script.AppendExtra('ifelse(is_substring("L720", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /system/rild/cdma/* /system/"));')
  info.script.AppendExtra('ifelse(is_substring("M919", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /system/rild/gsm/* /system/ && busybox rm /system/lib/libcnefeatureconfig.so"));')
  info.script.AppendExtra('ifelse(is_substring("R970", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /system/rild/usc/* /system/"));')
  info.script.AppendExtra('ifelse(is_substring("S970", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /system/rild/gsm/* /system/ && busybox rm /system/lib/libcnefeatureconfig.so"));')
  info.script.AppendExtra('ifelse(is_substring("S975", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /system/rild/gsm/* /system/ && busybox rm /system/lib/libcnefeatureconfig.so"));')
  info.script.AppendExtra('ifelse(is_substring("I9505", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /system/rild/gsm/* /system/ && busybox rm /system/lib/libcnefeatureconfig.so"));')
  info.script.AppendExtra('ifelse(is_substring("I9507", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /system/rild/gsm/* /system/ && busybox rm /system/lib/libcnefeatureconfig.so"));')
  info.script.AppendExtra('ifelse(is_substring("I9508", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /system/rild/gsm/* /system/ && busybox rm /system/lib/libcnefeatureconfig.so"));')
  info.script.AppendExtra('delete_recursive("/system/rild");')
  info.script.AppendExtra('set_metadata("/system/vendor/bin/efsks", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:mdm_helper_exec:s0");')
  info.script.AppendExtra('set_metadata("/system/vendor/bin/ks", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:mdm_helper_exec:s0");')
  info.script.AppendExtra('set_metadata("/system/vendor/bin/qcks", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:mdm_helper_exec:s0");')
  info.script.AppendExtra('set_metadata("/system/vendor/lib/libatparser.so", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:vendor_file:s0");')
  info.script.AppendExtra('set_metadata("/system/vendor/lib/libfactoryutil.so", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:vendor_file:s0");')
  info.script.AppendExtra('set_metadata("/system/vendor/lib/libomission_avoidance.so", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:vendor_file:s0");')
  info.script.AppendExtra('set_metadata("/system/vendor/lib/libreference-ril.so", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:vendor_file:s0");')
  info.script.AppendExtra('set_metadata("/system/vendor/lib/libsecril-client.so", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:vendor_file:s0");')
  info.script.AppendExtra('ifelse(is_substring("I545", getprop("ro.bootloader")),set_metadata("/system/vendor/lib/libcneapiclient.so", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:vendor_file:s0"));')
  info.script.AppendExtra('ifelse(is_substring("I545", getprop("ro.bootloader")),set_metadata("/system/vendor/lib/librmnetctl.so", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:vendor_file:s0"));')
  info.script.AppendExtra('ifelse(is_substring("L720", getprop("ro.bootloader")),set_metadata("/system/vendor/lib/libcneapiclient.so", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:vendor_file:s0"));')
  info.script.AppendExtra('ifelse(is_substring("L720", getprop("ro.bootloader")),set_metadata("/system/vendor/lib/librmnetctl.so", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:vendor_file:s0"));')
  info.script.AppendExtra('ifelse(is_substring("R970", getprop("ro.bootloader")),set_metadata("/system/vendor/lib/libcneapiclient.so", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:vendor_file:s0"));')
  info.script.AppendExtra('ifelse(is_substring("R970", getprop("ro.bootloader")),set_metadata("/system/vendor/lib/librmnetctl.so", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:vendor_file:s0"));')
  info.script.AppendExtra('ifelse(is_substring("I9505", getprop("ro.bootloader")),set_metadata("/system/vendor/lib/libril-qcril-external.so", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:vendor_file:s0"));')
  info.script.AppendExtra('ifelse(is_substring("I9507", getprop("ro.bootloader")),set_metadata("/system/vendor/lib/libril-qcril-external.so", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:vendor_file:s0"));')
  info.script.AppendExtra('ifelse(is_substring("I9508", getprop("ro.bootloader")),set_metadata("/system/vendor/lib/libril-qcril-external.so", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:vendor_file:s0"));')
  info.script.AppendExtra('ifelse(is_substring("S975", getprop("ro.bootloader")),set_metadata("/system/vendor/lib/libril-qcril-external.so", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:vendor_file:s0"));')
  info.script.AppendExtra('ifelse(is_substring("S970", getprop("ro.bootloader")),set_metadata("/system/vendor/lib/libril-qcril-external.so", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:vendor_file:s0"));')
  info.script.AppendExtra('ifelse(is_substring("M919", getprop("ro.bootloader")),set_metadata("/system/vendor/lib/libril-qcril-external.so", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:vendor_file:s0"));')
  info.script.AppendExtra('ifelse(is_substring("I337", getprop("ro.bootloader")),set_metadata("/system/vendor/lib/libril-qcril-external.so", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:vendor_file:s0"));')
  info.script.script = [cmd for cmd in info.script.script if not "boot.img" in cmd]
  info.script.script = [cmd for cmd in info.script.script if not "show_progress(0.100000, 0);" in cmd]
  info.script.AppendExtra('package_extract_file("boot.img", "/tmp/boot.img");')
  info.script.AppendExtra('assert(run_program("/sbin/sh", "/tmp/install/etc/loki.sh") == 0);')
  info.script.Unmount("/system")

def FullOTA_PostValidate(info):
    info.script.AppendExtra('run_program("/tmp/install/bin/e2fsck_static", "-fy", "/dev/block/platform/msm_sdcc.1/by-name/system");');
    info.script.AppendExtra('run_program("/tmp/install/bin/resize2fs_static", "/dev/block/platform/msm_sdcc.1/by-name/system");');
    info.script.AppendExtra('run_program("/tmp/install/bin/e2fsck_static", "-fy", "/dev/block/platform/msm_sdcc.1/by-name/system");');
