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

/**
 * Providing a Oauth2 Class and a ReplyServer for the Oauth2 authorization code flow. 
 */
#ifndef OAI_OAUTH2_H
#define OAI_OAUTH2_H

#include <QObject>
#include <QtCore>
#include <QtNetwork>
#include <QDesktopServices>
#include <QNetworkRequest>
#include <QNetworkReply>
#include <QNetworkAccessManager>
#include <QtDebug>
#include <QTcpServer>
#include <QTcpSocket>
#include <QByteArray>
#include <QString>
#include <QMap>
#include <QUrl>
#include <QUrlQuery>
#include <QDateTime>
#include <time.h>

namespace OpenAPI {

class oauthToken
{
public:
    oauthToken(QString token, int expiresIn, QString scope, QString tokenType) : m_token(token), m_scope(scope), m_type(tokenType){
        m_validUntil = time(nullptr) + expiresIn;
    }
    oauthToken(){
        m_validUntil = time(nullptr) - 1;
    }
    QString getToken(){return m_token;};
    QString getScope(){return m_scope;};
    QString getType(){return m_type;};
    bool isValid(){return time(nullptr) < m_validUntil;};

private:
    QString m_token;
    time_t m_validUntil;
    QString m_scope;
    QString m_type;
};

class ReplyServer : public QTcpServer
{
    Q_OBJECT
public:
    explicit ReplyServer(QObject *parent = nullptr);
    void setReply(QByteArray reply){m_reply = reply;};
    void run();
private:
    QByteArray m_reply;

Q_SIGNALS:
    void dataReceived(QMap<QString, QString>);

public Q_SLOTS:
    void onConnected();
    void read();
    void start();
    void stop();
};

//Base class
class OauthBase : public QObject
{
    Q_OBJECT
public: 
    OauthBase(QObject* parent = nullptr) : QObject(parent) {};
    oauthToken getToken(QString scope);
    void addToken(oauthToken token);
    void removeToken(QString scope);
    bool linked(){return m_linked;};
    virtual void link()=0;
    virtual void unlink()=0;

protected:
    QMap<QString, oauthToken> m_oauthTokenMap;
    QUrl m_authUrl;
    QUrl m_tokenUrl;
    QString m_scope, m_accessType, m_state, m_redirectUri, m_clientId, m_clientSecret;
    bool m_linked;

public Q_SLOTS:
    virtual void authenticationNeededCallback()=0;
    void onFinish(QNetworkReply *rep);

Q_SIGNALS:
    void authenticationNeeded();
    void tokenReceived();
};

// Authorization code flow
class OauthCode : public OauthBase
{
    Q_OBJECT
public:
    OauthCode(QObject *parent = nullptr);
    void link() override;
    void unlink() override;
    void setVariables(QString authUrl, QString tokenUrl, QString scope, QString state, QString redirectUri, QString clientId, QString clientSecret, QString accessType = "");

private:
    ReplyServer m_server;

public Q_SLOTS:
    void authenticationNeededCallback() override;
    void onVerificationReceived(const QMap<QString, QString> response);

};

// Implicit flow
class OauthImplicit : public OauthBase
{
    Q_OBJECT
public:
    OauthImplicit(QObject *parent = nullptr);
    void link() override;
    void unlink() override;
    void setVariables(QString authUrl, QString scope, QString state, QString redirectUri, QString clientId, QString accessType = "");

private:
    ReplyServer m_server;

public Q_SLOTS:
    void authenticationNeededCallback() override;
    void ImplicitTokenReceived(const QMap<QString, QString> response);
};

//client credentials flow
class OauthCredentials : public OauthBase
{
    Q_OBJECT
public:
    OauthCredentials(QObject *parent = nullptr);
    void link() override;
    void unlink() override;
    void setVariables(QString tokenUrl, QString scope, QString clientId, QString clientSecret);

public Q_SLOTS:
    void authenticationNeededCallback() override;

};

//resource owner password flow
class OauthPassword : public OauthBase
{
    Q_OBJECT
public:
    OauthPassword(QObject *parent = nullptr);
    void link() override;
    void unlink() override;
    void setVariables(QString tokenUrl, QString scope, QString clientId, QString clientSecret, QString username, QString password);

private:
    QString m_username, m_password;

public Q_SLOTS:
    void authenticationNeededCallback() override;

};


} // namespace OpenAPI
#endif // OAI_OAUTH2_H
