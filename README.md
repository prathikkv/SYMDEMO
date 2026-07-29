# orchestration-agent

Symphony agent service. Scaffolded by `eai-eng-repo-bootstrap`.

- Language: python
- Container registry: symphony.azurecr.io
- Deploy target: aks

## CI/CD
Pipeline: `azure-pipelines.yml` (4 stages: BuildAndTest → Containerize → Push → Deploy).
