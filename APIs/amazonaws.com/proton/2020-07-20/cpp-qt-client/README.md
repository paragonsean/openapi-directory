# C++ Qt API client

# 

AWS Proton

- API version: 2020-07-20
- Generator version: 7.9.0

<p>This is the Proton Service API Reference. It provides descriptions, syntax and usage examples for each of the <a href=\"https://docs.aws.amazon.com/proton/latest/APIReference/API_Operations.html\">actions</a> and <a href=\"https://docs.aws.amazon.com/proton/latest/APIReference/API_Types.html\">data types</a> for the Proton service.</p> <p>The documentation for each action shows the Query API request parameters and the XML response.</p> <p>Alternatively, you can use the Amazon Web Services CLI to access an API. For more information, see the <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html\">Amazon Web Services Command Line Interface User Guide</a>.</p> <p>The Proton service is a two-pronged automation framework. Administrators create service templates to provide standardized infrastructure and deployment tooling for serverless and container based applications. Developers, in turn, select from the available service templates to automate their application or service deployments.</p> <p>Because administrators define the infrastructure and tooling that Proton deploys and manages, they need permissions to use all of the listed API operations.</p> <p>When developers select a specific infrastructure and tooling set, Proton deploys their applications. To monitor their applications that are running on Proton, developers need permissions to the service <i>create</i>, <i>list</i>, <i>update</i> and <i>delete</i> API operations and the service instance <i>list</i> and <i>update</i> API operations.</p> <p>To learn more about Proton, see the <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/Welcome.html\">Proton User Guide</a>.</p> <p> <b>Ensuring Idempotency</b> </p> <p>When you make a mutating API request, the request typically returns a result before the asynchronous workflows of the operation are complete. Operations might also time out or encounter other server issues before they're complete, even if the request already returned a result. This might make it difficult to determine whether the request succeeded. Moreover, you might need to retry the request multiple times to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation occurs multiple times. This means that you might create more resources than you intended.</p> <p> <i>Idempotency</i> ensures that an API request action completes no more than one time. With an idempotent request, if the original request action completes successfully, any subsequent retries complete successfully without performing any further actions. However, the result might contain updated information, such as the current creation status.</p> <p>The following lists of APIs are grouped according to methods that ensure idempotency.</p> <p> <b>Idempotent create APIs with a client token</b> </p> <p>The API actions in this list support idempotency with the use of a <i>client token</i>. The corresponding Amazon Web Services CLI commands also support idempotency using a client token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request using one of these actions, specify a client token in the request. We recommend that you <i>don't</i> reuse the same client token for other API requests. If you don’t provide a client token for these APIs, a default client token is automatically provided by SDKs.</p> <p>Given a request action that has succeeded:</p> <p>If you retry the request using the same client token and the same parameters, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.</p> <p>If you retry the request using the same client token, but one or more of the parameters are different, the retry throws a <code>ValidationException</code> with an <code>IdempotentParameterMismatch</code> error.</p> <p>Client tokens expire eight hours after a request is made. If you retry the request with the expired token, a new resource is created.</p> <p>If the original resource is deleted and you retry the request, a new resource is created.</p> <p>Idempotent create APIs with a client token:</p> <ul> <li> <p>CreateEnvironmentTemplateVersion</p> </li> <li> <p>CreateServiceTemplateVersion</p> </li> <li> <p>CreateEnvironmentAccountConnection</p> </li> </ul> <p> <b>Idempotent create APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>If you retry the request with an API from this group, and the original resource <i>hasn't</i> been modified, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.</p> <p>If the original resource has been modified, the retry throws a <code>ConflictException</code>.</p> <p>If you retry with different input parameters, the retry throws a <code>ValidationException</code> with an <code>IdempotentParameterMismatch</code> error.</p> <p>Idempotent create APIs:</p> <ul> <li> <p>CreateEnvironmentTemplate</p> </li> <li> <p>CreateServiceTemplate</p> </li> <li> <p>CreateEnvironment</p> </li> <li> <p>CreateService</p> </li> </ul> <p> <b>Idempotent delete APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>When you retry the request with an API from this group and the resource was deleted, its metadata is returned in the response.</p> <p>If you retry and the resource doesn't exist, the response is empty.</p> <p>In both cases, the retry succeeds.</p> <p>Idempotent delete APIs:</p> <ul> <li> <p>DeleteEnvironmentTemplate</p> </li> <li> <p>DeleteEnvironmentTemplateVersion</p> </li> <li> <p>DeleteServiceTemplate</p> </li> <li> <p>DeleteServiceTemplateVersion</p> </li> <li> <p>DeleteEnvironmentAccountConnection</p> </li> </ul> <p> <b>Asynchronous idempotent delete APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>If you retry the request with an API from this group, if the original request delete operation status is <code>DELETE_IN_PROGRESS</code>, the retry returns the resource detail data in the response without performing any further actions.</p> <p>If the original request delete operation is complete, a retry returns an empty response.</p> <p>Asynchronous idempotent delete APIs:</p> <ul> <li> <p>DeleteEnvironment</p> </li> <li> <p>DeleteService</p> </li> </ul>

  For more information, please visit [https://github.com/mermade/aws2openapi](https://github.com/mermade/aws2openapi)

*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:

1. CMake 3.2+
2. Qt
3. C++ Compiler

## Getting Started

example.h:
```c++

#include <iostream>
#include "../client/OAIDefaultApi.h"

using namespace test_namespace;

class Example : public QObject {
    Q_OBJECT
    QString create();
    OAIAcceptEnvironmentAccountConnectionInput create();
    QString create();
    QString create();
    QString create();
    QString create();
    QString create();
    QString create();
    QString create();
public Q_SLOTS:
   void exampleFunction1();
};

```

example.cpp:
```c++

#include "../client/OAIDefaultApi.h"
#include "example.h"
#include <QTimer>
#include <QEventLoop>

QString Example::create(){
    QString obj;
OAIAcceptEnvironmentAccountConnectionInput Example::create(){
    OAIAcceptEnvironmentAccountConnectionInput obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
 return obj;
}

void Example::exampleFunction1(){
     OAIDefaultApi apiInstance;
     
      // Configure API key authorization: hmac
      apiInstance.setApiKey("YOUR API KEY NAME","YOUR API KEY");

      QEventLoop loop;
      connect(&apiInstance, &OAIDefaultApi::acceptEnvironmentAccountConnectionSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIDefaultApi::acceptEnvironmentAccountConnectionSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString x_amz_target = create(); // QString | 

      QEventLoop loop;
      connect(&apiInstance, &OAIDefaultApi::acceptEnvironmentAccountConnectionSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIDefaultApi::acceptEnvironmentAccountConnectionSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      OAIAcceptEnvironmentAccountConnectionInput oai_accept_environment_account_connection_input = create(); // OAIAcceptEnvironmentAccountConnectionInput | 

      QEventLoop loop;
      connect(&apiInstance, &OAIDefaultApi::acceptEnvironmentAccountConnectionSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIDefaultApi::acceptEnvironmentAccountConnectionSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString x_amz_content_sha256 = create(); // QString | 

      QEventLoop loop;
      connect(&apiInstance, &OAIDefaultApi::acceptEnvironmentAccountConnectionSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIDefaultApi::acceptEnvironmentAccountConnectionSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString x_amz_date = create(); // QString | 

      QEventLoop loop;
      connect(&apiInstance, &OAIDefaultApi::acceptEnvironmentAccountConnectionSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIDefaultApi::acceptEnvironmentAccountConnectionSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString x_amz_algorithm = create(); // QString | 

      QEventLoop loop;
      connect(&apiInstance, &OAIDefaultApi::acceptEnvironmentAccountConnectionSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIDefaultApi::acceptEnvironmentAccountConnectionSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString x_amz_credential = create(); // QString | 

      QEventLoop loop;
      connect(&apiInstance, &OAIDefaultApi::acceptEnvironmentAccountConnectionSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIDefaultApi::acceptEnvironmentAccountConnectionSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString x_amz_security_token = create(); // QString | 

      QEventLoop loop;
      connect(&apiInstance, &OAIDefaultApi::acceptEnvironmentAccountConnectionSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIDefaultApi::acceptEnvironmentAccountConnectionSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString x_amz_signature = create(); // QString | 

      QEventLoop loop;
      connect(&apiInstance, &OAIDefaultApi::acceptEnvironmentAccountConnectionSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIDefaultApi::acceptEnvironmentAccountConnectionSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString x_amz_signed_headers = create(); // QString | 
      apiInstance.acceptEnvironmentAccountConnection(x_amz_targetoai_accept_environment_account_connection_inputx_amz_content_sha256x_amz_datex_amz_algorithmx_amz_credentialx_amz_security_tokenx_amz_signaturex_amz_signed_headers);
      QTimer::singleShot(5000, &loop, &QEventLoop::quit);
      loop.exec();
  }

```

## Documentation for Servers

Parameterized Servers are supported. Define a server in the API for each endpoint with arbitrary numbers of variables:

```yaml
servers:
- url: http://{server}:{port}/{basePath}
  description: Description of the Server
  variables:
    server:
        enum:
          - 'petstore'
          - 'qa-petstore'
          - 'dev-petstore'
        default: 'petstore'
    port:
      enum:
        - '3000'
        - '1000'
      default: '3000'
    basePath:
      default: v1
```
To change the default variable, use this function in each Api:
```c++
int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
```
The parameter "serverIndex" will choose a server from the server list for each endpoint. There is always at least one server with index 0. The Parameter "operation" should be the desired endpoint operationid.
Variable is the name of the variable you wish to change and the value is the new default Value.
The function will return -1 when the variable does not exists, -2 if value is not defined in the variable enum and -3 if the operation is not found.

If your endpoint has multiple server objects in the servers array, you can set the server that will be used with this function:
```c++
void setServerIndex(const QString &operation, int serverIndex);
```
Parameter "operation" should be your operationid. "serverIndex" is the index you want to set as your default server. The function will check if there is a server with your index.
Here is an example of multiple servers in the servers array. The first server will have index 0 and the second will have index 1.
```yaml
servers:
- url: http://{server}:8080/
  description: Description of the Server
  variables:
    server:
        enum:
          - 'petstore'
          - 'qa-petstore'
          - 'dev-petstore'
        default: 'petstore'
- url: https://localhost:8080/v1
```

## Documentation for Authorization

Authentication schemes defined for the API:
### hmac


- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

mike.ralphson@gmail.com


## License

Apache 2.0 License for more information visit [Apache 2.0 License](http://www.apache.org/licenses/)