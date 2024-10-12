/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIUpdateNetworkAppliancePrefixesDelegatedStatic_request.h
 *
 * 
 */

#ifndef OAIUpdateNetworkAppliancePrefixesDelegatedStatic_request_H
#define OAIUpdateNetworkAppliancePrefixesDelegatedStatic_request_H

#include <QJsonObject>

#include "OAICreateNetworkAppliancePrefixesDelegatedStatic_request_origin.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICreateNetworkAppliancePrefixesDelegatedStatic_request_origin;

class OAIUpdateNetworkAppliancePrefixesDelegatedStatic_request : public OAIObject {
public:
    OAIUpdateNetworkAppliancePrefixesDelegatedStatic_request();
    OAIUpdateNetworkAppliancePrefixesDelegatedStatic_request(QString json);
    ~OAIUpdateNetworkAppliancePrefixesDelegatedStatic_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    OAICreateNetworkAppliancePrefixesDelegatedStatic_request_origin getOrigin() const;
    void setOrigin(const OAICreateNetworkAppliancePrefixesDelegatedStatic_request_origin &origin);
    bool is_origin_Set() const;
    bool is_origin_Valid() const;

    QString getPrefix() const;
    void setPrefix(const QString &prefix);
    bool is_prefix_Set() const;
    bool is_prefix_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    OAICreateNetworkAppliancePrefixesDelegatedStatic_request_origin m_origin;
    bool m_origin_isSet;
    bool m_origin_isValid;

    QString m_prefix;
    bool m_prefix_isSet;
    bool m_prefix_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateNetworkAppliancePrefixesDelegatedStatic_request)

#endif // OAIUpdateNetworkAppliancePrefixesDelegatedStatic_request_H
