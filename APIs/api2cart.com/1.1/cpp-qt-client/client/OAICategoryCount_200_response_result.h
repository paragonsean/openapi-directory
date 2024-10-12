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
 * OAICategoryCount_200_response_result.h
 *
 * 
 */

#ifndef OAICategoryCount_200_response_result_H
#define OAICategoryCount_200_response_result_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICategoryCount_200_response_result : public OAIObject {
public:
    OAICategoryCount_200_response_result();
    OAICategoryCount_200_response_result(QString json);
    ~OAICategoryCount_200_response_result() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getCategoriesCount() const;
    void setCategoriesCount(const qint32 &categories_count);
    bool is_categories_count_Set() const;
    bool is_categories_count_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_categories_count;
    bool m_categories_count_isSet;
    bool m_categories_count_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICategoryCount_200_response_result)

#endif // OAICategoryCount_200_response_result_H
