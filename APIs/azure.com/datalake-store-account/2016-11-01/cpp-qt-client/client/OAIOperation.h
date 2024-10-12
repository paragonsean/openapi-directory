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
 * OAIOperation.h
 *
 * An available operation for Data Lake Store.
 */

#ifndef OAIOperation_H
#define OAIOperation_H

#include <QJsonObject>

#include "OAIOperationDisplay.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIOperationDisplay;

class OAIOperation : public OAIObject {
public:
    OAIOperation();
    OAIOperation(QString json);
    ~OAIOperation() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIOperationDisplay getDisplay() const;
    void setDisplay(const OAIOperationDisplay &display);
    bool is_display_Set() const;
    bool is_display_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getOrigin() const;
    void setOrigin(const QString &origin);
    bool is_origin_Set() const;
    bool is_origin_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIOperationDisplay m_display;
    bool m_display_isSet;
    bool m_display_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_origin;
    bool m_origin_isSet;
    bool m_origin_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOperation)

#endif // OAIOperation_H
