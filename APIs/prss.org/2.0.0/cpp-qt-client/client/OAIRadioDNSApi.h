/**
 * ContentDepot
 * ContentDepot hosts a range of API’s that allow clients to manage, discover, and obtain content. The API spans many parts of the ContentDepot functionality including MetaPub (a.k.a. metadata distribution) and content management.  ## MetaPub  MetaPub collects, normalizes and distributes publicly available program, episode, and piece metadata through the public radio system. Backed by ContentDepot and its data model, MetaPub allows producers to supply metadata through various methods:  1. MetaPub Agents that collect producer metadata by \"crawling\" existing public feeds (e.g. C24, BBC) or the producer's production system (e.g. ATC, ME, TED Radio Hour). 2. Manually enter metadata in the ContentDepot Portal on each program and episode. 3. Publish/push the metadata to the MetaPub upload API and execute an ingest job.  MetaPub then distributes this data to stations through an electronic program guide (EPG model) for display on various listener devices such as smart phones, tablets, web streams, HD radios, RDBS enabled FM radios, and more. The EPG format is based on the RadioDNS specifications.  ### RadioDNS  The RadioDNS Service and Programme Information Specification ([ETSI TS 102 818 v3.4.1](https://www.etsi.org/deliver/etsi_ts/102800_102899/102818/03.04.01_60/ts_102818v030401p.pdf)) defines three primary documents: Service Information, Program Information, and Group Information. These documents, along with the core RadioDNS Hybrid Lookup for Radio Services Specification ([ETSI TS 103 270 v1.4.1](https://www.etsi.org/deliver/etsi_ts/103200_103299/103270/01.04.01_60/ts_103270v010401p.pdf)), define a system where an end listener device can dynamically discover program metadata and fetch the metadata via Internet Protocol (IP) requests. MetaPub's use of RadioDNS differs slightly in that MetaPub (a.k.a PRSS) acts as the \"service provider\" while the stations and related middleware act as the end devices. While this is not the primary use case of RadioDNS, the flexibility in the specification, service definitions, and DNS resolution allows this model to be easily represented. MetaPub provides both _National Metadata_ and _Station Metadata_.  It is strongly recommended that the related [RadioDNS specifications](https://radiodns.org/developers/documentation/) be read for implementation details, definitions, and required XML schemas.  ## ContentDepot Drive  ContentDepot Drive (CD Drive) provides a private, per customer file storage solution similar to other cloud storage solutions such as Google Drive, Box, and Dropbox. The CD Drive is used to stage content uploads such as metadata files, images, or segment audio before associating the content with specific programs or episodes.  CD Drive content can be referenced using a URI by some operations such as synchronizing metadata. There are two possible CD Drive URI formats supported: ID and hierarchical path. The ID reference takes the form ```cddrive:id:{value}``` where value is the integer ID of the file or folder being referenced. The hierarchical path reference takes the form ```cddrive://{path}``` where path is the full, UNIX style path to the file or folder starting with '/'. For example, two CD Drive URIs pointing to the same file may be ```cddrive:id:12345``` and ```cddrive:///show1/episode2/metadata.xml```. More information about URIs can be found at [Wikipedia](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier).  ## Authentication  The API currently uses OAuth 2.0.  All operations require ```cd:full``` access where the client access is only limited by the permissions of the ContentDepot user after authentication. Limiting access scope per client is not currently supported. 
 *
 * The version of the OpenAPI document: 2.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIRadioDNSApi_H
#define OAI_OAIRadioDNSApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIRadioDNSApi : public QObject {
    Q_OBJECT

public:
    OAIRadioDNSApi(const int timeOut = 0);
    ~OAIRadioDNSApi();

    void initializeServerConfigs();
    int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
    void setServerIndex(const QString &operation, int serverIndex);
    void setApiKey(const QString &apiKeyName, const QString &apiKey);
    void setBearerToken(const QString &token);
    void setUsername(const QString &username);
    void setPassword(const QString &password);
    void setTimeOut(const int timeOut);
    void setWorkingDirectory(const QString &path);
    void setNetworkAccessManager(QNetworkAccessManager* manager);
    int addServerConfiguration(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables = QMap<QString, OAIServerVariable>());
    void setNewServerForAllOperations(const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void setNewServer(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void addHeaders(const QString &key, const QString &value);
    void enableRequestCompression();
    void enableResponseCompression();
    void abortRequests();
    QString getParamStylePrefix(const QString &style);
    QString getParamStyleSuffix(const QString &style);
    QString getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode);


    virtual void radiodnsSpi31GIXmlGet();

    /**
    * @param[in]  fqdn QString [required]
    * @param[in]  sid QString [required]
    * @param[in]  date QString [required]
    * @param[in]  x_radiodnsspi_api_key QString [optional]
    */
    virtual void radiodnsSpi31IdFqdnSidDatePIXmlGet(const QString &fqdn, const QString &sid, const QString &date, const ::OpenAPI::OptionalParam<QString> &x_radiodnsspi_api_key = ::OpenAPI::OptionalParam<QString>());


    virtual void radiodnsSpi31SIXmlGet();


private:
    QMap<QString,int> _serverIndices;
    QMap<QString,QList<OAIServerConfiguration>> _serverConfigs;
    QMap<QString, QString> _apiKeys;
    QString _bearerToken;
    QString _username;
    QString _password;
    int _timeOut;
    QString _workingDirectory;
    QNetworkAccessManager* _manager;
    QMap<QString, QString> _defaultHeaders;
    bool _isResponseCompressionEnabled;
    bool _isRequestCompressionEnabled;
    OAIHttpRequestInput _latestInput;
    OAIHttpRequestWorker *_latestWorker;
    QStringList _latestScope;
    OauthCode _authFlow;
    OauthImplicit _implicitFlow;
    OauthCredentials _credentialFlow;
    OauthPassword _passwordFlow;
    int _OauthMethod = 0;

    void radiodnsSpi31GIXmlGetCallback(OAIHttpRequestWorker *worker);
    void radiodnsSpi31IdFqdnSidDatePIXmlGetCallback(OAIHttpRequestWorker *worker);
    void radiodnsSpi31SIXmlGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void radiodnsSpi31GIXmlGetSignal(QString summary);
    void radiodnsSpi31IdFqdnSidDatePIXmlGetSignal(QString summary);
    void radiodnsSpi31SIXmlGetSignal(QString summary);


    void radiodnsSpi31GIXmlGetSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void radiodnsSpi31IdFqdnSidDatePIXmlGetSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void radiodnsSpi31SIXmlGetSignalFull(OAIHttpRequestWorker *worker, QString summary);

    Q_DECL_DEPRECATED_X("Use radiodnsSpi31GIXmlGetSignalError() instead")
    void radiodnsSpi31GIXmlGetSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void radiodnsSpi31GIXmlGetSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use radiodnsSpi31IdFqdnSidDatePIXmlGetSignalError() instead")
    void radiodnsSpi31IdFqdnSidDatePIXmlGetSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void radiodnsSpi31IdFqdnSidDatePIXmlGetSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use radiodnsSpi31SIXmlGetSignalError() instead")
    void radiodnsSpi31SIXmlGetSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void radiodnsSpi31SIXmlGetSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use radiodnsSpi31GIXmlGetSignalErrorFull() instead")
    void radiodnsSpi31GIXmlGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void radiodnsSpi31GIXmlGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use radiodnsSpi31IdFqdnSidDatePIXmlGetSignalErrorFull() instead")
    void radiodnsSpi31IdFqdnSidDatePIXmlGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void radiodnsSpi31IdFqdnSidDatePIXmlGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use radiodnsSpi31SIXmlGetSignalErrorFull() instead")
    void radiodnsSpi31SIXmlGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void radiodnsSpi31SIXmlGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
