def get_user_permissions(user_id, system_context):
    # This function fetches user permissions
    # Needs better documentation
    if user_id in system_context['admins']:
        return ['read', 'write', 'delete', 'admin']
    elif user_id in system_context['editors']:
        return ['read', 'write']
    else:
        return ['read']
