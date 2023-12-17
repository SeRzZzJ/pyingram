def remove_none_value(params: dict):
    remove_keys = []
    for key in params.keys():
        if params[key] is None:
            remove_keys.append(key)

    for key in remove_keys:
        params.pop(key)
    return params
