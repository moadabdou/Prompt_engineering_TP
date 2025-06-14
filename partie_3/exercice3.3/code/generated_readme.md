
## **Utility: `get_user_permissions`**

This utility function determines a user's permissions based on their role (administrator, editor, or standard user).

---

### **Function Signature**

```python
def get_user_permissions(user_id: int | str, system_context: dict) -> list[str]:
```

**Parameters**

* `user_id` (`int` | `str`): The unique identifier for the user.
* `system_context` (`dict`): A dictionary defining user roles. It **must** contain the following keys:
    * `'admins'` (`list`): A list of user IDs with administrator rights.
    * `'editors'` (`list`): A list of user IDs with editor rights.

**Return Value**

* A list of strings (`list[str]`) representing the user's permissions.

---

### **Permission Levels**

The permissions returned are based on the user's role:

* **Administrator**: `['read', 'write', 'delete', 'admin']`
* **Editor**: `['read', 'write']`
* **Standard User**: `['read']` (default if the user is not an admin or editor)

---

### **Example Usage**

Here’s how to use the function. Assume it's located in `utils/permissions.py`.

```python
# Import the function
from utils.permissions import get_user_permissions

# 1. Define the system context
system_context = {
    'admins': [10, 25],
    'editors': [101, 105, 210],
    # The 'users' key is optional and ignored by the function
    'users': [1, 2, 3, 4]
}

# 2. Get permissions for an administrator
admin_id = 10
admin_permissions = get_user_permissions(admin_id, system_context)
print(f"Permissions for admin ID {admin_id}: {admin_permissions}")
# Expected: ['read', 'write', 'delete', 'admin']

# 3. Get permissions for an editor
editor_id = 105
editor_permissions = get_user_permissions(editor_id, system_context)
print(f"Permissions for editor ID {editor_id}: {editor_permissions}")
# Expected: ['read', 'write']

# 4. Get permissions for a standard user
user_id = 999
user_permissions = get_user_permissions(user_id, system_context)
print(f"Permissions for user ID {user_id}: {user_permissions}")
# Expected: ['read']
```