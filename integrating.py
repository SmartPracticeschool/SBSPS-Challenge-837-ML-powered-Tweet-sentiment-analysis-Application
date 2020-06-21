from watson_machine_learning_client import WatsonMachineLearningAPIClient
wml_credentials={
    
  "apikey": "4vnrkEnrIEd4CuKhvsE6n4ln688R9KsTRJF0e1ToLhin",
  "iam_apikey_description": "Auto-generated for key f69890e6-5d4f-4198-b8b6-4d3c031c2b9b",
  "iam_apikey_name": "Service credentials-1",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Writer",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/a620725bef1a43228159e9d3ed10249d::serviceid:ServiceId-125284e7-abf4-4cad-b2d8-a24fb3815438",
  "instance_id": "f57f3fd7-4886-4469-bb29-5c3dc3752753",
  "url": "https://eu-gb.ml.cloud.ibm.com"
}
client=WatsonMachineLearningAPIClient(wml_credentials)
model_props={
    client.repository.ModelMetaNames.AUTHOR_NAME:"Sabrina",
    client.repository.ModelMetaNames.AUTHOR_EMAIL:"sshaik_it171251@mgit.ac.in",
    client.repository.ModelMetaNames.NAME:"Twittes sentimental analysis"
    
}
model_artifact=client.repository.store_model(model,meta_props = model_props)
model_artifact
guid=client.repository.get_model_uid(model_artifact)
guid
scoring_url=client.deployments.get_scoring_url(deploy)
scoring_url
