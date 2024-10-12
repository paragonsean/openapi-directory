/**
 * Runscope API
 * Manage Runscope programmatically.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAI_buckets__bucketKey__tests_get_200_response.h
 *
 * 
 */

#ifndef OAI_buckets__bucketKey__tests_get_200_response_H
#define OAI_buckets__bucketKey__tests_get_200_response_H

#include <QJsonObject>

#include "OAIMeta.h"
#include "OAITest.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAITest;
class OAIMeta;

class OAI_buckets__bucketKey__tests_get_200_response : public OAIObject {
public:
    OAI_buckets__bucketKey__tests_get_200_response();
    OAI_buckets__bucketKey__tests_get_200_response(QString json);
    ~OAI_buckets__bucketKey__tests_get_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAITest> getData() const;
    void setData(const QList<OAITest> &data);
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

    QList<OAITest> m_data;
    bool m_data_isSet;
    bool m_data_isValid;

    OAIMeta m_meta;
    bool m_meta_isSet;
    bool m_meta_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAI_buckets__bucketKey__tests_get_200_response)

#endif // OAI_buckets__bucketKey__tests_get_200_response_H
