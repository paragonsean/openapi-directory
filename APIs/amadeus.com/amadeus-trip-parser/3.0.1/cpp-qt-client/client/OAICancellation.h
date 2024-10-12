/**
 * Trip Parser
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 3.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICancellation.h
 *
 * 
 */

#ifndef OAICancellation_H
#define OAICancellation_H

#include <QJsonObject>

#include "OAIDescription.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIDescription;

class OAICancellation : public OAIObject {
public:
    OAICancellation();
    OAICancellation(QString json);
    ~OAICancellation() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIDescription getDescription() const;
    void setDescription(const OAIDescription &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIDescription m_description;
    bool m_description_isSet;
    bool m_description_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICancellation)

#endif // OAICancellation_H
