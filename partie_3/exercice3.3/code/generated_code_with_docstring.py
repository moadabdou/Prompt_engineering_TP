def get_user_permissions(user_id, system_context):
    """Récupère la liste des permissions pour un utilisateur donné.

    Cette fonction vérifie le niveau d'autorisation d'un utilisateur
    (administrateur, éditeur, ou utilisateur standard) en se basant sur le
    contexte du système et retourne les permissions correspondantes.

    Args:
        user_id (int or str): L'identifiant unique de l'utilisateur.
        system_context (dict): Un dictionnaire contenant les listes
            d'utilisateurs. Doit contenir les clés 'admins' et 'editors',
            chacune associée à une liste d'identifiants utilisateurs.
            Exemple :
            {
                'admins': [1, 101],
                'editors': [2, 202, 303]
            }

    Returns:
        list[str]: Une liste de chaînes de caractères représentant les
                   permissions accordées à l'utilisateur.
                   - ['read', 'write', 'delete', 'admin'] pour les administrateurs.
                   - ['read', 'write'] pour les éditeurs.
                   - ['read'] pour tous les autres utilisateurs.

    Example:
        >>> context = {
        ...     'admins': [10, 25],
        ...     'editors': [101, 105, 210],
        ...     'users': [1, 2, 3]
        ... }
        >>>
        >>> # Test pour un administrateur
        >>> get_user_permissions(10, context)
        ['read', 'write', 'delete', 'admin']
        >>>
        >>> # Test pour un éditeur
        >>> get_user_permissions(105, context)
        ['read', 'write']
        >>>
        >>> # Test pour un utilisateur standard
        >>> get_user_permissions(3, context)
        ['read']
    """
    if user_id in system_context.get('admins', []):
        return ['read', 'write', 'delete', 'admin']
    elif user_id in system_context.get('editors', []):
        return ['read', 'write']
    else:
        return ['read']