/**
 * agentOS Api V2, Customer Login Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-customer
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAILandlordProfitLossSectionModel.h
 *
 * Class for a group of entries.
 */

#ifndef OAILandlordProfitLossSectionModel_H
#define OAILandlordProfitLossSectionModel_H

#include <QJsonObject>

#include "OAILandlordProfitLossRowModel.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAILandlordProfitLossRowModel;

class OAILandlordProfitLossSectionModel : public OAIObject {
public:
    OAILandlordProfitLossSectionModel();
    OAILandlordProfitLossSectionModel(QString json);
    ~OAILandlordProfitLossSectionModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAILandlordProfitLossRowModel> getRows() const;
    void setRows(const QList<OAILandlordProfitLossRowModel> &rows);
    bool is_rows_Set() const;
    bool is_rows_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAILandlordProfitLossRowModel> m_rows;
    bool m_rows_isSet;
    bool m_rows_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILandlordProfitLossSectionModel)

#endif // OAILandlordProfitLossSectionModel_H
