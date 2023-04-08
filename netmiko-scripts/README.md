# Venv for netmiko/paramiko testing

This venv is used by both Windows and MacOS. venv script files are ignored.

## Script for testing commands

Scripts for testing netmiko/paramiko commands without dependencies on other files, and inheritance from other classes.

```txt
ios_xe_config_common.py
ios_xr_config_common.py
nxos_config_common.py
```

## Configuration commands

All device configuration files are stored in `device_cfg_files` directory.

***_config.py** - runs commands from .cfg files.

***_verify.py** - runs device 'show' commands.

***_verify_textfsm.py** - runs device 'show' commands agains prebuilt textfsm templates from ntc-templates repository which netconf library uses by default.

***_config_revert** - runs commands from .cfg files in order to revert previous configurtion.