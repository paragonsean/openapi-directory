/**
 * Bufferapp
 * Social media management for marketers and agencies
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIConfiguration_services_facebook_urls.h
 *
 * 
 */

#ifndef OAIConfiguration_services_facebook_urls_H
#define OAIConfiguration_services_facebook_urls_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIConfiguration_services_facebook_urls : public OAIObject {
public:
    OAIConfiguration_services_facebook_urls();
    OAIConfiguration_services_facebook_urls(QString json);
    ~OAIConfiguration_services_facebook_urls() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getUser() const;
    void setUser(const QString &user);
    bool is_user_Set() const;
    bool is_user_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_user;
    bool m_user_isSet;
    bool m_user_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIConfiguration_services_facebook_urls)

#endif // OAIConfiguration_services_facebook_urls_H
