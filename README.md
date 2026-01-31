# Ansible Role: Harbor

Installs and configures [Harbor](https://goharbor.io/), an open-source container image registry, on Linux.

## Requirements

* Ansible 2.10+
* Docker and Docker Compose installed on the target host
* Supported platforms:
  * Amazon Linux
  * Debian
  * Ubuntu
  * Enterprise Linux (RHEL, CentOS, Rocky, Alma)

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml` and `vars/main.yml`).

### Required Variables

These variables **must** be set — the role will fail if they are not provided:

| Variable | Description |
|---|---|
| `harbor_hostname` | The hostname for the Harbor registry (e.g., `registry.example.com`) |
| `harbor_external_url` | The external URL for Harbor (e.g., `https://registry.example.com`) |
| `harbor_admin_password` | The password for the Harbor admin user. Use `ansible-vault` to encrypt this value |

### General

| Variable | Default | Description |
|---|---|---|
| `harbor_version_release` | `2.8.2` | The release version of Harbor to install |
| `harbor_version_config` | `2.8.0` | The configuration version of Harbor |
| `harbor_installation_dir` | `/etc/harbor` | The directory where Harbor will be installed |
| `harbor_http_port` | `80` | The HTTP port on which Harbor will be accessible |
| `harbor_admin_password` | `''` | The password for the default admin user (**required**) |
| `harbor_data_volume` | `/data` | The volume path for storing Harbor data |
| `harbor_user` | `root` | The user that will own the Harbor installation |
| `harbor_run_installer` | `true` | Whether to run the Harbor install script. Set to `false` for testing |

### Storage Service

| Variable | Default | Description |
|---|---|---|
| `harbor_storage_service_cache_layerinfo` | `redis` | Caching layer information service |
| `harbor_storage_service_delete_enabled` | `true` | Enable the delete operation for Harbor storage |
| `harbor_storage_service_maintenance_uploadpurging_age` | `168h` | The age of uploaded files before purging |
| `harbor_storage_service_maintenance_uploadpurging_dryrun` | `false` | Run purging in dry-run mode |
| `harbor_storage_service_maintenance_uploadpurging_enabled` | `true` | Enable upload purging maintenance |
| `harbor_storage_service_maintenance_uploadpurging_interval` | `24h` | Interval between purging runs |
| `harbor_storage_service_redirect_disable` | `false` | Disable redirection in storage service |

#### S3 Storage Configuration

| Variable | Default | Description |
|---|---|---|
| `harbor_storage_service_s3_accesskey` | `''` | Access key for S3 storage |
| `harbor_storage_service_s3_secretkey` | `''` | Secret key for S3 storage |
| `harbor_storage_service_s3_bucket` | `''` | S3 bucket name |
| `harbor_storage_service_s3_region` | `''` | S3 region |
| `harbor_storage_service_s3_chunksize` | `5242880` | S3 chunk size |
| `harbor_storage_service_s3_multipartcopychunksize` | `33554432` | S3 multipart copy chunk size |
| `harbor_storage_service_s3_multipartcopymaxconcurrency` | `100` | S3 multipart copy max concurrency |
| `harbor_storage_service_s3_multipartcopythresholdsize` | `33554432` | S3 multipart copy threshold size |
| `harbor_storage_service_s3_secure` | `true` | Enable HTTPS for S3 |

### Job Service

| Variable | Default | Description |
|---|---|---|
| `harbor_jobservice_logger_sweeper_duration` | `10` | The duration for the job service logger sweeper |
| `harbor_jobservice_max_job_workers` | `1` | Maximum number of job workers |

### Notification

| Variable | Default | Description |
|---|---|---|
| `harbor_notification_webhook_job_http_client_timeout` | `3` | HTTP client timeout for webhook jobs |
| `harbor_notification_webhook_job_max_retry` | `3` | Maximum retry attempts for webhook jobs |

### Logging

| Variable | Default | Description |
|---|---|---|
| `harbor_log_level` | `info` | Log level for Harbor (`debug`, `info`, `warning`, `error`, `fatal`) |
| `harbor_log_local_location` | `/var/log/harbor` | Local file system location for Harbor logs |
| `harbor_log_local_rotate_count` | `10` | Number of rotated log files to keep |
| `harbor_log_local_rotate_size` | `200M` | Size at which log files are rotated |

### External Database

| Variable | Default | Description |
|---|---|---|
| `harbor_external_database_enabled` | `false` | Enable usage of an external database |
| `harbor_external_database_harbor_db_name` | `harbor` | Name of the external Harbor database |
| `harbor_external_database_harbor_host` | `''` | Host address for the external database |
| `harbor_external_database_harbor_port` | `5432` | Port number for the external database |
| `harbor_external_database_harbor_username` | `''` | Username for the external database |
| `harbor_external_database_harbor_password` | `''` | Password for the external database |
| `harbor_external_database_harbor_ssl_mode` | `disable` | SSL mode (`disable`, `require`, `verify-ca`, `verify-full`) |
| `harbor_external_database_harbor_max_idle_conns` | `100` | Maximum idle connections |
| `harbor_external_database_harbor_max_open_conns` | `900` | Maximum open connections |

### External Redis

| Variable | Default | Description |
|---|---|---|
| `harbor_external_redis_enabled` | `false` | Enable usage of an external Redis server |
| `harbor_external_redis_host` | `''` | Host address for the external Redis server |
| `harbor_external_redis_jobservice_db_index` | `2` | Database index for job service data |
| `harbor_external_redis_registry_db_index` | `1` | Database index for registry data |

### Proxy

| Variable | Default | Description |
|---|---|---|
| `harbor_proxy_components` | `['core', 'jobservice', 'trivy']` | Components to use the proxy |
| `harbor_proxy_http_proxy` | `''` | HTTP proxy server |
| `harbor_proxy_https_proxy` | `''` | HTTPS proxy server |
| `harbor_proxy_no_proxy` | `''` | Domains or IPs to exclude from proxying |

### Metrics

| Variable | Default | Description |
|---|---|---|
| `harbor_metric_enabled` | `false` | Enable Prometheus metrics |
| `harbor_metric_path` | `/metrics` | Metrics endpoint path |
| `harbor_metric_port` | `9090` | Metrics endpoint port |

### Upload Purging

| Variable | Default | Description |
|---|---|---|
| `harbor_upload_purging_enabled` | `true` | Enable upload purging |
| `harbor_upload_purging_age` | `168h` | Age of uploads before purging |
| `harbor_upload_purging_dryrun` | `false` | Run purging in dry-run mode |
| `harbor_upload_purging_interval` | `24h` | Interval between purging runs |

### Cache

| Variable | Default | Description |
|---|---|---|
| `harbor_cache_enabled` | `true` | Enable caching |
| `harbor_cache_expire_hours` | `24` | Cache expiration time in hours |

### Custom Properties

| Variable | Default | Description |
|---|---|---|
| `harbor_custom_properties` | `{}` | Additional properties merged into the final Harbor configuration |

## Dependencies

None.

## Example Playbook

### Minimal

```yaml
- hosts: all
  roles:
    - role: ansible-role-harbor
      harbor_hostname: "registry.example.com"
      harbor_external_url: "https://registry.example.com"
      harbor_admin_password: "{{ vault_harbor_admin_password }}"
```

### With external database and Redis

```yaml
- hosts: all
  roles:
    - role: ansible-role-harbor
      harbor_hostname: "registry.example.com"
      harbor_external_url: "https://registry.example.com"
      harbor_admin_password: "{{ vault_harbor_admin_password }}"
      harbor_external_database_enabled: true
      harbor_external_database_harbor_host: "db.example.com"
      harbor_external_database_harbor_username: "harbor"
      harbor_external_database_harbor_password: "{{ vault_harbor_db_password }}"
      harbor_external_database_harbor_ssl_mode: "require"
      harbor_external_redis_enabled: true
      harbor_external_redis_host: "redis.example.com"
```

### With S3 storage backend

```yaml
- hosts: all
  roles:
    - role: ansible-role-harbor
      harbor_hostname: "registry.example.com"
      harbor_external_url: "https://registry.example.com"
      harbor_admin_password: "{{ vault_harbor_admin_password }}"
      harbor_storage_service_s3_accesskey: "{{ vault_s3_access_key }}"
      harbor_storage_service_s3_secretkey: "{{ vault_s3_secret_key }}"
      harbor_storage_service_s3_bucket: "harbor-registry"
      harbor_storage_service_s3_region: "us-east-1"
```

## License

MIT

## Author Information

This role was created by [ialejandro](https://github.com/ialejandro).
