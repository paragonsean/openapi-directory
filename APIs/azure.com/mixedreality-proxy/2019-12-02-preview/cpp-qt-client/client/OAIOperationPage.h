/**
 * Mixed Reality
 * Mixed Reality Resource Provider Proxy API
 *
 * The version of the OpenAPI document: 2019-12-02-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIOperationPage.h
 *
 * Result of the request to list Resource Provider operations. It contains a list of operations and a URL link to get the next set of results.
 */

#ifndef OAIOperationPage_H
#define OAIOperationPage_H

#include <QJsonObject>

#include "OAIOperation.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIOperation;

class OAIOperationPage : public OAIObject {
public:
    OAIOperationPage();
    OAIOperationPage(QString json);
    ~OAIOperationPage() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getNextLink() const;
    void setNextLink(const QString &next_link);
    bool is_next_link_Set() const;
    bool is_next_link_Valid() const;

    QList<OAIOperation> getValue() const;
    void setValue(const QList<OAIOperation> &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_next_link;
    bool m_next_link_isSet;
    bool m_next_link_isValid;

    QList<OAIOperation> m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOperationPage)

#endif // OAIOperationPage_H
