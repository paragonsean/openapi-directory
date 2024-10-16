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
 * OAIConfiguration_services_google.h
 *
 * 
 */

#ifndef OAIConfiguration_services_google_H
#define OAIConfiguration_services_google_H

#include <QJsonObject>

#include "OAIConfiguration_services_facebook_urls.h"
#include "OAIConfiguration_services_google_types.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIConfiguration_services_google_types;
class OAIConfiguration_services_facebook_urls;

class OAIConfiguration_services_google : public OAIObject {
public:
    OAIConfiguration_services_google();
    OAIConfiguration_services_google(QString json);
    ~OAIConfiguration_services_google() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIConfiguration_services_google_types getTypes() const;
    void setTypes(const OAIConfiguration_services_google_types &types);
    bool is_types_Set() const;
    bool is_types_Valid() const;

    OAIConfiguration_services_facebook_urls getUrls() const;
    void setUrls(const OAIConfiguration_services_facebook_urls &urls);
    bool is_urls_Set() const;
    bool is_urls_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIConfiguration_services_google_types m_types;
    bool m_types_isSet;
    bool m_types_isValid;

    OAIConfiguration_services_facebook_urls m_urls;
    bool m_urls_isSet;
    bool m_urls_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIConfiguration_services_google)

#endif // OAIConfiguration_services_google_H
