# Setting Up Minikube with PostgreSQL and Web Application Using Helm

## Prerequisites

- **Minikube**: Ensure Minikube is installed. Follow the [official documentation](https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download) to set it up.
- **kubectl**: Configure an alias for convenience:
  ```bash
  alias kubectl="minikube kubectl --"
  ```

---

## Step 1: Start Minikube

Start your Minikube cluster:

```bash
minikube start
```

## Step 2: Inventory App Helm Chart

### 1. Create the Helm Chart

Create a Helm chart named `inventory-app` in your project directory.

- Replace the `templates/` directory with the required Kubernetes resource files, such as `deployment.yaml`, `statefulset.yaml`, `service.yaml`, `pvc.yaml`, `secrets.yaml`, and other necessary files.
- Update the `helpers.tpl` file to include functions that dynamically generate useful names.
- Modify `values.yaml` to define application-specific configurations like database details, image settings, and replica counts.

### 2. Deploy or Upgrade the Application

To install or upgrade the `inventory-app` release, run the following command:

```bash
helm upgrade --install inventory-management-app . \
  --namespace inventory-app\
  --create-namespace \
  --set appuser.username=<your-username> \
  --set appuser.userpassword=<your-password> \
  --set postgres.auth.password=<your-password>

```

The --create-namespace flag will ensure that the namespace inventory-app-ns is created if it does not already exist.
This command will install the inventory-app release or upgrade it if it's already installed.

For running the more generalized version use the following command.

```bash
helm upgrade --install inventory-management-app . \
  --namespace inventory-app  \
  --create-namespace  \
  --set-string configMap[0].user.userName="<your-postgres-username>"  \
  --set-string configMap[0].db.dbName="<your-database-name>"  \
  --set-string secret[0].value="<your-postgres-root-password>"  \
  --set-string secret[1].value="<your-postgres-user-password>"  \
  -f values.yaml
```

Note: In this case use user-password as same as root-password.
