/**
 * Azure SQL Database
 * Provides create, read, update and delete functionality for Azure SQL Database resources including recommendations and operations.
 *
 * The version of the OpenAPI document: 2014-04-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITransparentDataEncryptionActivityListResult.h
 *
 * Represents the response to a list database transparent data encryption activity request.
 */

#ifndef OAITransparentDataEncryptionActivityListResult_H
#define OAITransparentDataEncryptionActivityListResult_H

#include <QJsonObject>

#include "OAITransparentDataEncryptionActivity.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAITransparentDataEncryptionActivity;

class OAITransparentDataEncryptionActivityListResult : public OAIObject {
public:
    OAITransparentDataEncryptionActivityListResult();
    OAITransparentDataEncryptionActivityListResult(QString json);
    ~OAITransparentDataEncryptionActivityListResult() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAITransparentDataEncryptionActivity> getValue() const;
    void setValue(const QList<OAITransparentDataEncryptionActivity> &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAITransparentDataEncryptionActivity> m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITransparentDataEncryptionActivityListResult)

#endif // OAITransparentDataEncryptionActivityListResult_H
