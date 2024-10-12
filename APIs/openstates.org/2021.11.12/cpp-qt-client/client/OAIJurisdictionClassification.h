/**
 * Open States API v3
 *  * [More documentation](https://docs.openstates.org/en/latest/api/v3/index.html) * [Register for an account](https://openstates.org/accounts/signup/)   **We are currently working to restore experimental support for committees & events.**  During this period please note that data is not yet available for all states and the exact format of the new endpoints may change slightly depending on user feedback.  If you have any issues or questions use our [GitHub Issues](https://github.com/openstates/issues/issues) to give feedback. 
 *
 * The version of the OpenAPI document: 2021.11.12
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIJurisdictionClassification.h
 *
 * An enumeration.
 */

#ifndef OAIJurisdictionClassification_H
#define OAIJurisdictionClassification_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIJurisdictionClassification : public OAIEnum {
public:
    OAIJurisdictionClassification();
    OAIJurisdictionClassification(QString json);
    ~OAIJurisdictionClassification() override;

    QString asJson() const override;
    QJsonValue asJsonValue() const override;
    void fromJsonValue(QJsonValue json) override;
    void fromJson(QString jsonString) override;

    enum class eOAIJurisdictionClassification {
        INVALID_VALUE_OPENAPI_GENERATED = 0,
        STATE, 
        MUNICIPALITY, 
        COUNTRY
    };
    OAIJurisdictionClassification::eOAIJurisdictionClassification getValue() const;
    void setValue(const OAIJurisdictionClassification::eOAIJurisdictionClassification& value);
    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    eOAIJurisdictionClassification m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIJurisdictionClassification)

#endif // OAIJurisdictionClassification_H
