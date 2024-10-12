/**
 * LH Public API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAirportResource.h
 *
 * Root element of airport response.
 */

#ifndef OAIAirportResource_H
#define OAIAirportResource_H

#include <QJsonObject>

#include "OAIAirportResource_Airports.h"
#include "OAIAirportResource_Meta.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAirportResource_Airports;
class OAIAirportResource_Meta;

class OAIAirportResource : public OAIObject {
public:
    OAIAirportResource();
    OAIAirportResource(QString json);
    ~OAIAirportResource() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAirportResource_Airports getAirports() const;
    void setAirports(const OAIAirportResource_Airports &airports);
    bool is_airports_Set() const;
    bool is_airports_Valid() const;

    OAIAirportResource_Meta getMeta() const;
    void setMeta(const OAIAirportResource_Meta &meta);
    bool is_meta_Set() const;
    bool is_meta_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAirportResource_Airports m_airports;
    bool m_airports_isSet;
    bool m_airports_isValid;

    OAIAirportResource_Meta m_meta;
    bool m_meta_isSet;
    bool m_meta_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAirportResource)

#endif // OAIAirportResource_H
