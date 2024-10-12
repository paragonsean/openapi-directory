/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFailoverSetsList.h
 *
 * The list of failover sets.
 */

#ifndef OAIFailoverSetsList_H
#define OAIFailoverSetsList_H

#include <QJsonObject>

#include "OAIFailoverSet.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIFailoverSet;

class OAIFailoverSetsList : public OAIObject {
public:
    OAIFailoverSetsList();
    OAIFailoverSetsList(QString json);
    ~OAIFailoverSetsList() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIFailoverSet> getValue() const;
    void setValue(const QList<OAIFailoverSet> &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIFailoverSet> m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFailoverSetsList)

#endif // OAIFailoverSetsList_H
