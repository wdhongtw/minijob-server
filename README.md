## Development Guideline

### Generate / Update Client Library

Generate OpenAPI schema `openapi.json`

```shell
python generate.py openapi.json
```

Assume the server / client project is named `minijob-server` / `minijob-client`

Generate client project and library

```shell
# Client project name can be controlled in generator-config file
pipx run openapi-python-client \
    --config minijob-server/res/generator-config \
    generate \
    --path minijob-server/openapi.json
```

Update client project and library

```shell
# Client project name can be controlled in generator-config file
pipx run openapi-python-client \
    --config minijob-server/res/generator-config \
    update \
    --path minijob-server/openapi.json
```


