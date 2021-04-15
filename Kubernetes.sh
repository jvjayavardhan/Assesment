#!/bin/sh

# Author : Jayavardhan Bairabathina
# Problem : Create a Kubernetes pod. Write a shell script to restart the Kubernetes pod, Fetch logs from the Kubernetes pod , Test if pods are running and finally print the running status of the Pod.
#--------------------------------
# Pre-requisites:               -
#--------------------------------
# minikube installed            -
# kubectl installed             -
# start the minikube with command [minikube start --vm-driver=hyperkit] which will start the default k8s master in VM
#--------------------------------

#To create a new pod
kubectl create deployment ubuntu-depl --image=ubuntu

#To restart existing pod
kubectl scale deployment ubuntu-depl --replicas=0
kubectl scale deployment ubuntu-depl --replicas=1

POD_NAME = kubectl get pods --sort-by=.metadata.creationTimestamp -o jsonpath="{.items[0].metadata.name}"

kubectl logs POD_NAME

POD_STATUS = kubectl get pods POD_NAME --no-headers -o custom-columns=":status.phase"

if [ "$POD_STATUS" == "Running" ]; then
    echo "Pod is Running"
else
    echo "Pod Status: $POD_STATUS"
fi