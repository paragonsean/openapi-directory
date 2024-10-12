/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIProviderOperationResult.h
 *
 * Result of the request to list REST API operations
 */

#ifndef OAIProviderOperationResult_H
#define OAIProviderOperationResult_H

#include <QJsonObject>

#include "OAIOperationMetadata.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIOperationMetadata;

class OAIProviderOperationResult : public OAIObject {
public:
    OAIProviderOperationResult();
    OAIProviderOperationResult(QString json);
    ~OAIProviderOperationResult() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getNextLink() const;
    void setNextLink(const QString &next_link);
    bool is_next_link_Set() const;
    bool is_next_link_Valid() const;

    QList<OAIOperationMetadata> getValue() const;
    void setValue(const QList<OAIOperationMetadata> &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_next_link;
    bool m_next_link_isSet;
    bool m_next_link_isValid;

    QList<OAIOperationMetadata> m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProviderOperationResult)

#endif // OAIProviderOperationResult_H
