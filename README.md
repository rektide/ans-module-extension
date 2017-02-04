# Ansible Module Extension

[./action_plugins/include_vars2.py](./action_plugins/include_vars2.py) is supposed to "extend" include_vars. While it produces similar ansible_facts output, running a debug on the output produces different results: the include_vars2 result is not interpolated, unlike include_vars.

I'd like to understand what is going on here, and figure out how to extend another module without breaking basic functionality.

# Sample output

```
TASK [include_vars2] ***********************************************************
task path: /home/rektide/src/ans-module-extension/example.yml:6
ok: [localhost] => {"ansible_facts": {"myVariable": "my number is {{myNumber}}"}, "changed": false}

TASK [debug] *******************************************************************
task path: /home/rektide/src/ans-module-extension/example.yml:9
ok: [localhost] => {
    "msg": "my number is {{myNumber}}"
}

TASK [include_vars] ************************************************************
task path: /home/rektide/src/ans-module-extension/example.yml:10
ok: [localhost] => {"ansible_facts": {"myVariable": "my number is {{myNumber}}"}, "changed": false}

TASK [debug] *******************************************************************
task path: /home/rektide/src/ans-module-extension/example.yml:13
ok: [localhost] => {
    "msg": "my number is 45"
}

PLAY RECAP *********************************************************************
localhost                  : ok=5    changed=0    unreachable=0    failed=0   
```
