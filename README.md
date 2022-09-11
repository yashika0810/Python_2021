### Database sync script: 

This section holds the instructions to run the `database.sh` script in order to pull and restore the database. You can find this script in `bin/database.sh` 

#### 1. Please make sure you configure AWS CLI and you have  [yq](https://github.com/mikefarah/yq) installed in your local.

#### 2. Pass this argument while running script
       `gpg-path`: Pass s3 url `s3://infra...` or the `GPG_KEY.asc` file path on your local. 

> NOTE: Please pass the s3 url in the gpg-path flag if GPG_FILE.asc does not exist on your local. Once it downloads the file in your local env, you can pass the file path. 


#### command:

```
./bin/database.sh pull —-gpg-path <gpg_key_path/s3 url>

```

#### example:
``` 
./bin/database.sh pull —-gpg-path GPG_KEY.asc 

```
> NOTE: The default env is set to production. You can change it to staging by changing the SECRET_FILE variable path to "secrets.staging.enc.yaml" in the script. 

If you want to override your local username and password, it can be passed as env variable which is OPTIONAL.

#### command:
```
LOCAL_USER=<username> PGPASSWORD=<local_password> LOCAL_DB=<db_name> ./bin/database.sh pull —-gpg-path <gpg_key_path/s3 url>

```




