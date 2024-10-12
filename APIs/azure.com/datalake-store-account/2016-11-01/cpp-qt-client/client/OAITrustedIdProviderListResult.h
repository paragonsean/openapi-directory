/**
 * DataLakeStoreAccountManagementClient
 * Creates an Azure Data Lake Store account management client.
 *
 * The version of the OpenAPI document: 2016-11-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITrustedIdProviderListResult.h
 *
 * Data Lake Store trusted identity provider list information.
 */

#ifndef OAITrustedIdProviderListResult_H
#define OAITrustedIdProviderListResult_H

#include <QJsonObject>

#include "OAITrustedIdProvider.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAITrustedIdProvider;

class OAITrustedIdProviderListResult : public OAIObject {
public:
    OAITrustedIdProviderListResult();
    OAITrustedIdProviderListResult(QString json);
    ~OAITrustedIdProviderListResult() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getNextLink() const;
    void setNextLink(const QString &next_link);
    bool is_next_link_Set() const;
    bool is_next_link_Valid() const;

    QList<OAITrustedIdProvider> getValue() const;
    void setValue(const QList<OAITrustedIdProvider> &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_next_link;
    bool m_next_link_isSet;
    bool m_next_link_isValid;

    QList<OAITrustedIdProvider> m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITrustedIdProviderListResult)

#endif // OAITrustedIdProviderListResult_H
