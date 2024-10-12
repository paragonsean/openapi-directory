/**
 * Trip Purpose Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 1.1.4
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPrediction.h
 *
 * 
 */

#ifndef OAIPrediction_H
#define OAIPrediction_H

#include <QJsonObject>

#include "OAIMeta.h"
#include "OAIPurpose_Prediction.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPurpose_Prediction;
class OAIMeta;

class OAIPrediction : public OAIObject {
public:
    OAIPrediction();
    OAIPrediction(QString json);
    ~OAIPrediction() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIPurpose_Prediction getData() const;
    void setData(const OAIPurpose_Prediction &data);
    bool is_data_Set() const;
    bool is_data_Valid() const;

    OAIMeta getMeta() const;
    void setMeta(const OAIMeta &meta);
    bool is_meta_Set() const;
    bool is_meta_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIPurpose_Prediction m_data;
    bool m_data_isSet;
    bool m_data_isValid;

    OAIMeta m_meta;
    bool m_meta_isSet;
    bool m_meta_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPrediction)

#endif // OAIPrediction_H
