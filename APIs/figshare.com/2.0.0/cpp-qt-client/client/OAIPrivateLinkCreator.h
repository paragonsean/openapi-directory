/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPrivateLinkCreator.h
 *
 * 
 */

#ifndef OAIPrivateLinkCreator_H
#define OAIPrivateLinkCreator_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPrivateLinkCreator : public OAIObject {
public:
    OAIPrivateLinkCreator();
    OAIPrivateLinkCreator(QString json);
    ~OAIPrivateLinkCreator() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getExpiresDate() const;
    void setExpiresDate(const QString &expires_date);
    bool is_expires_date_Set() const;
    bool is_expires_date_Valid() const;

    bool isReadOnly() const;
    void setReadOnly(const bool &read_only);
    bool is_read_only_Set() const;
    bool is_read_only_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_expires_date;
    bool m_expires_date_isSet;
    bool m_expires_date_isValid;

    bool m_read_only;
    bool m_read_only_isSet;
    bool m_read_only_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPrivateLinkCreator)

#endif // OAIPrivateLinkCreator_H
