/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIErrorAttachmentLocation.h
 *
 * 
 */

#ifndef OAIErrorAttachmentLocation_H
#define OAIErrorAttachmentLocation_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIErrorAttachmentLocation : public OAIObject {
public:
    OAIErrorAttachmentLocation();
    OAIErrorAttachmentLocation(QString json);
    ~OAIErrorAttachmentLocation() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getUri() const;
    void setUri(const QString &uri);
    bool is_uri_Set() const;
    bool is_uri_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_uri;
    bool m_uri_isSet;
    bool m_uri_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIErrorAttachmentLocation)

#endif // OAIErrorAttachmentLocation_H
