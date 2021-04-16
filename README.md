# kubeconfig-exporter
A simple script to convert/export CA/KEY/CERT from .kube/config


### convert files paths into base64 encoded data
```
python kubeconfig.py --to-data -f ~/.kube/config
```

from:

```
apiVersion: v1
clusters:
- cluster:
    certificate-authority: /root/.minikube/ca.crt
    server: https://10.140.0.3:8443
  name: minikube
contexts:
- context:
    cluster: minikube
    namespace: default
    user: minikube
  name: minikube
current-context: minikube
kind: Config
preferences: {}
users:
- name: minikube
  user:
    client-certificate: /root/.minikube/profiles/minikube/client.crt
    client-key: /root/.minikube/profiles/minikube/client.key
```
to 

```
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: xxxxxx
    server: https://10.140.0.3:8443
  name: minikube
contexts:
- context:
    cluster: minikube
    namespace: default
    user: minikube
  name: minikube
current-context: minikube
kind: Config
preferences: {}
users:
- name: minikube
  user:
    client-certificate-data: xxxx
    client-key-data: xxxx
```

