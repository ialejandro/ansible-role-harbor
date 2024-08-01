# Ansible Role: Harbor

Installs and configures [Harbor](https://goharbor.io/), an open-source container image registry, on Linux.

## Requirements

* Ansible 2.10+
* Supported platforms:
  * Amazon Linux
  * Other platforms might be supported but have not been tested.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml` and `vars/main.yml`):

### General

* `harbor_version_release`: The release version of Harbor to install.
  * **Default**: `2.8.2`
  * **Example**:

    ```yaml
    harbor_version_release: 2.8.2
    ```

* `harbor_version_config`: The configuration version of Harbor.
  * **Default**: `2.8.0`
  * **Example**:

    ```yaml
    harbor_version_config: 2.8.0
    ```

* `harbor_installation_dir`: The directory where Harbor will be installed.
  * **Default**: `/etc/harbor`
  * **Example**:

    ```yaml
    harbor_installation_dir: /etc/harbor
    ```

* `harbor_http_port`: The HTTP port on which Harbor will be accessible.
  * **Default**: `80`
  * **Example**:

    ```yaml
    harbor_http_port: 8080
    ```

* `harbor_admin_password`: The password for the default admin user in Harbor.
  * **Default**: `myawesomepassword`
  * **Example**:

    ```yaml
    harbor_admin_password: securepassword123
    ```

* `harbor_data_volume`: The volume path for storing Harbor data.
  * **Default**: `/data`
  * **Example**:

    ```yaml
    harbor_data_volume: /mnt/harbor_data
    ```

* `harbor_user`: The user that will own the Harbor installation.
  * **Default**: `root`
  * **Example**:

    ```yaml
    harbor_user: harbor
    ```

### Storage Service

* `harbor_storage_service_cache_layerinfo`: Caching layer information service.
  * **Default**: `redis`
  * **Example**:

    ```yaml
    harbor_storage_service_cache_layerinfo: memcached
    ```

* `harbor_storage_service_delete_enabled`: Enable the delete operation for Harbor storage.
  * **Default**: `true`
  * **Example**:

    ```yaml
    harbor_storage_service_delete_enabled: false
    ```

* `harbor_storage_service_maintenance_uploadpurging_age`: The age of uploaded files before purging.
  * **Default**: `168h` (7 days)
  * **Example**:

    ```yaml
    harbor_storage_service_maintenance_uploadpurging_age: 72h
    ```

* `harbor_storage_service_maintenance_uploadpurging_dryrun`: Run purging in dry-run mode.
  * **Default**: `false`
  * **Example**:

    ```yaml
    harbor_storage_service_maintenance_uploadpurging_dryrun: true
    ```

* `harbor_storage_service_redirect_disable`: Disable redirection in storage service.
  * **Default**: `false`
  * **Example**:

    ```yaml
    harbor_storage_service_redirect_disable: true
    ```

#### S3 Storage Configuration

* `harbor_storage_service_s3_accesskey`: Access key for S3 storage.
  * **Default**: `""` (Empty, requires setting)
  * **Example**:

    ```yaml
    harbor_storage_service_s3_accesskey: YOUR_ACCESS_KEY
    ```

* `harbor_storage_service_s3_secretkey`: Secret key for S3 storage.
  * **Default**: `""` (Empty, requires setting)
  * **Example**:

    ```yaml
    harbor_storage_service_s3_secretkey: YOUR_SECRET_KEY
    ```

* `harbor_storage_service_s3_bucket`: S3 bucket name.
  * **Default**: `""` (Empty, requires setting)
  * **Example**:

    ```yaml
    harbor_storage_service_s3_bucket: harbor-bucket
    ```

* `harbor_storage_service_s3_region`: S3 region.
  * **Default**: `""` (Empty, requires setting)
  * **Example**:

    ```yaml
    harbor_storage_service_s3_region: us-west-1
    ```

### Job Service

* `harbor_jobservice_logger_sweeper_duration`: The duration for the job service logger sweeper.
  * **Default**: `10`
  * **Example**:

    ```yaml
    harbor_jobservice_logger_sweeper_duration: 15
    ```

* `harbor_jobservice_max_job_workers`: Maximum number of job workers.
  * **Default**: `1`
  * **Example**:

    ```yaml
    harbor_jobservice_max_job_workers: 5
    ```

### Notification

* `harbor_notification_webhook_job_http_client_timeout`: HTTP client timeout for webhook jobs.
  * **Default**: `3`
  * **Example**:

    ```yaml
    harbor_notification_webhook_job_http_client_timeout: 5
    ```

* `harbor_notification_webhook_job_max_retry`: Maximum retry attempts for webhook jobs.
  * **Default**: `3`
  * **Example**:

    ```yaml
    harbor_notification_webhook_job_max_retry: 5
    ```

### Logging

* `harbor_log_level`: Log level for Harbor.
  * **Default**: `info`
  * **Example**:

    ```yaml
    harbor_log_level: debug
    ```

* `harbor_log_local_location`: Local file system location for Harbor logs.
  * **Default**: `/var/log/harbor`
  * **Example**:

    ```yaml
    harbor_log_local_location: /opt/harbor/logs
    ```

* `harbor_log_local_rotate_count`: Number of rotated log files to keep.
  * **Default**: `10`
  * **Example**:

    ```yaml
    harbor_log_local_rotate_count: 5
    ```

* `harbor_log_local_rotate_size`: Size at which log files are rotated.
  * **Default**: `200M`
  * **Example**:

    ```yaml
    harbor_log_local_rotate_size: 100M
    ```

### External Database

* `harbor_external_database_enabled`: Enable usage of an external database.
  * **Default**: `false`
  * **Example**:

    ```yaml
    harbor_external_database_enabled: true
    ```

* `harbor_external_database_harbor_db_name`: Name of the external Harbor database.
  * **Default**: `harbor`
  * **Example**:

    ```yaml
    harbor_external_database_harbor_db_name: harbor_db
    ```

* `harbor_external_database_harbor_host`: Host address for the external Harbor database.
  * **Default**: `""` (Empty, requires setting)
  * **Example**:

    ```yaml
    harbor_external_database_harbor_host: db.example.com
    ```

* `harbor_external_database_harbor_max_idle_conns`: Maximum idle connections to the external database.
  * **Default**: `100`
  * **Example**:

    ```yaml
    harbor_external_database_harbor_max_idle_conns: 50
    ```

* `harbor_external_database_harbor_max_open_conns`: Maximum open connections to the external database.
  * **Default**: `900`
  * **Example**:

    ```yaml
    harbor_external_database_harbor_max_open_conns: 300
    ```

* `harbor_external_database_harbor_password`: Password for the external Harbor database user.
  * **Default**: `""` (Empty, requires setting)
  * **Example**:

    ```yaml
    harbor_external_database_harbor_password: db_password
    ```

* `harbor_external_database_harbor_port`: Port number for the external Harbor database.
  * **Default**: `5432`
  * **Example**:

    ```yaml
    harbor_external_database_harbor_port: 3306
    ```

* `harbor_external_database_harbor_ssl_mode`: SSL mode for connecting to the external Harbor database.
  * **Default**: `disable`
  * **Example**:

    ```yaml
    harbor_external_database_harbor_ssl_mode: require
    ```

* `harbor_external_database_harbor_username`: Username for the external Harbor database.
  * **Default**: `""` (Empty, requires setting)
  * **Example**:

    ```yaml
    harbor_external_database_harbor_username: db_user
    ```

### External Redis

* `harbor_external_redis_enabled`: Enable usage of an external Redis server.
  * **Default**: `false`
  * **Example**:

    ```yaml
    harbor_external_redis_enabled: true
    ```

* `harbor_external_redis_host`: Host address for the external Redis server.
  * **Default**: `""` (Empty, requires setting)
  * **Example**:

    ```yaml
    harbor_external_redis_host: redis.example.com
    ```

* `harbor_external_redis_jobservice_db_index`: Database index for job service data.
  * **Default**: `2`
  * **Example**:

    ```yaml
    harbor_external_redis_jobservice_db_index: 3
    ```

* `harbor_external_redis_registry_db_index`: Database index for registry data.
  * **Default**: `1`
  * **Example**:

    ```yaml
    harbor_external_redis_registry_db_index: 2
    ```

### Proxy

* `harbor_proxy_components`: Components to use the proxy.
  * **Default**: `['core', 'jobservice', 'trivy']`
  * **Example**:

    ```yaml
    harbor_proxy_components: ['core', 'jobservice']
    ```

* `harbor_proxy_http_proxy`: HTTP proxy server.
  * **Default**: `""` (Empty, requires setting)
  * **Example**:

    ```yaml
    harbor_proxy_http_proxy: http://proxy.example.com:8080
    ```

* `harbor_proxy_https_proxy`: HTTPS proxy server.
  * **Default**: `""` (Empty, requires setting)
  * **Example**:

    ```yaml
    harbor_proxy_https_proxy: https://proxy.example.com:8443
    ```

* `harbor_proxy_no_proxy`: Domains or IPs to exclude from proxying.
  * **Default**: `""` (Empty, requires setting)
  * **Example**:

    ```yaml
    harbor_proxy_no_proxy: "localhost,127.0.0.1,.example.com"
    ```

### Metrics

* `harbor_metric_enabled`: Enable Prometheus metrics.
  * **Default**: `false`
  * **Example**:

    ```yaml
    harbor_metric_enabled: true
    ```

* `harbor_metric_path`: Metrics path.
  * **Default**: `/metrics`
  * **Example**:

    ```yaml
    harbor_metric_path: /custom/metrics
    ```

* `harbor_metric_port`: Metrics port.
  * **Default**: `9090`
  * **Example**:

    ```yaml
    harbor_metric_port: 9100
    ```

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: ansible-role-harbor
      harbor_admin_password: "securepassword123"
      harbor_external_database_enabled: true
      harbor_external_database_harbor_host: "db.example.com"
      harbor_external_database_harbor_username: "harbor"
      harbor_external_database_harbor_password: "db_password"
      harbor_external_database_harbor_port: 5432
      harbor_external_database_harbor_ssl_mode: "require"
```

## License

MIT

## Author Information

This role was created by [ialejandro](https://github.com/ialejandro).
