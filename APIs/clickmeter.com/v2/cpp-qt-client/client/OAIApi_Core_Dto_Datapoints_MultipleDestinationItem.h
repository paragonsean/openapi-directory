/**
 * ClickMeter API
 * Api dashboard for ClickMeter API
 *
 * The version of the OpenAPI document: v2
 * Contact: api@clickmeter.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIApi_Core_Dto_Datapoints_MultipleDestinationItem.h
 *
 * 
 */

#ifndef OAIApi_Core_Dto_Datapoints_MultipleDestinationItem_H
#define OAIApi_Core_Dto_Datapoints_MultipleDestinationItem_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIApi_Core_Dto_Datapoints_MultipleDestinationItem : public OAIObject {
public:
    OAIApi_Core_Dto_Datapoints_MultipleDestinationItem();
    OAIApi_Core_Dto_Datapoints_MultipleDestinationItem(QString json);
    ~OAIApi_Core_Dto_Datapoints_MultipleDestinationItem() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIApi_Core_Dto_Datapoints_MultipleDestinationItem)

#endif // OAIApi_Core_Dto_Datapoints_MultipleDestinationItem_H
