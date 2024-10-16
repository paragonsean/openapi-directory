/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFormattedEnumType_SEPPLifeExpectancyTable.h
 *
 * 
 */

#ifndef OAIFormattedEnumType_SEPPLifeExpectancyTable_H
#define OAIFormattedEnumType_SEPPLifeExpectancyTable_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIFormattedEnumType_SEPPLifeExpectancyTable : public OAIObject {
public:
    OAIFormattedEnumType_SEPPLifeExpectancyTable();
    OAIFormattedEnumType_SEPPLifeExpectancyTable(QString json);
    ~OAIFormattedEnumType_SEPPLifeExpectancyTable() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getValue() const;
    void setValue(const QString &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFormattedEnumType_SEPPLifeExpectancyTable)

#endif // OAIFormattedEnumType_SEPPLifeExpectancyTable_H
