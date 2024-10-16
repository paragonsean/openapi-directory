/**
 * Football Prediction API
 * The Football Prediction API allows developers to get predictions for upcoming football (soccer) matches, results for past matches, and performance monitoring for statistical models.
 *
 * The version of the OpenAPI document: 2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAI_api_v2_list_federations_get_404_response_errors_inner.h
 *
 * 
 */

#ifndef OAI_api_v2_list_federations_get_404_response_errors_inner_H
#define OAI_api_v2_list_federations_get_404_response_errors_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAI_api_v2_list_federations_get_404_response_errors_inner : public OAIObject {
public:
    OAI_api_v2_list_federations_get_404_response_errors_inner();
    OAI_api_v2_list_federations_get_404_response_errors_inner(QString json);
    ~OAI_api_v2_list_federations_get_404_response_errors_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getColumnWithErrors() const;
    void setColumnWithErrors(const QString &column_with_errors);
    bool is_column_with_errors_Set() const;
    bool is_column_with_errors_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_column_with_errors;
    bool m_column_with_errors_isSet;
    bool m_column_with_errors_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAI_api_v2_list_federations_get_404_response_errors_inner)

#endif // OAI_api_v2_list_federations_get_404_response_errors_inner_H
