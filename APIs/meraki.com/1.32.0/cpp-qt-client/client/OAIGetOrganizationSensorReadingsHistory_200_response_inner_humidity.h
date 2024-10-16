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
 * OAIGetOrganizationSensorReadingsHistory_200_response_inner_humidity.h
 *
 * Reading for the &#39;humidity&#39; metric. This will only be present if the &#39;metric&#39; property equals &#39;humidity&#39;.
 */

#ifndef OAIGetOrganizationSensorReadingsHistory_200_response_inner_humidity_H
#define OAIGetOrganizationSensorReadingsHistory_200_response_inner_humidity_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGetOrganizationSensorReadingsHistory_200_response_inner_humidity : public OAIObject {
public:
    OAIGetOrganizationSensorReadingsHistory_200_response_inner_humidity();
    OAIGetOrganizationSensorReadingsHistory_200_response_inner_humidity(QString json);
    ~OAIGetOrganizationSensorReadingsHistory_200_response_inner_humidity() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getRelativePercentage() const;
    void setRelativePercentage(const qint32 &relative_percentage);
    bool is_relative_percentage_Set() const;
    bool is_relative_percentage_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_relative_percentage;
    bool m_relative_percentage_isSet;
    bool m_relative_percentage_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetOrganizationSensorReadingsHistory_200_response_inner_humidity)

#endif // OAIGetOrganizationSensorReadingsHistory_200_response_inner_humidity_H
