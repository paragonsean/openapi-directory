/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAttributeUpdate_200_response_result.h
 *
 * 
 */

#ifndef OAIAttributeUpdate_200_response_result_H
#define OAIAttributeUpdate_200_response_result_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAttributeUpdate_200_response_result : public OAIObject {
public:
    OAIAttributeUpdate_200_response_result();
    OAIAttributeUpdate_200_response_result(QString json);
    ~OAIAttributeUpdate_200_response_result() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isUpdated() const;
    void setUpdated(const bool &updated);
    bool is_updated_Set() const;
    bool is_updated_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_updated;
    bool m_updated_isSet;
    bool m_updated_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAttributeUpdate_200_response_result)

#endif // OAIAttributeUpdate_200_response_result_H
