/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIBadResponse.h
 *
 * An HTTP response that is not supposed to be returned by a service
 */

#ifndef OAIBadResponse_H
#define OAIBadResponse_H

#include <QJsonObject>

#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIBadResponse : public OAIObject {
public:
    OAIBadResponse();
    OAIBadResponse(QString json);
    ~OAIBadResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBody() const;
    void setBody(const QString &body);
    bool is_body_Set() const;
    bool is_body_Valid() const;

    QMap<QString, QString> getHeaders() const;
    void setHeaders(const QMap<QString, QString> &headers);
    bool is_headers_Set() const;
    bool is_headers_Valid() const;

    qint32 getStatus() const;
    void setStatus(const qint32 &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_body;
    bool m_body_isSet;
    bool m_body_isValid;

    QMap<QString, QString> m_headers;
    bool m_headers_isSet;
    bool m_headers_isValid;

    qint32 m_status;
    bool m_status_isSet;
    bool m_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBadResponse)

#endif // OAIBadResponse_H
