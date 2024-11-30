SELECT
    user_id,
    user_group
FROM users
where 1=1
    AND login = '$login'
    AND password = '$password'