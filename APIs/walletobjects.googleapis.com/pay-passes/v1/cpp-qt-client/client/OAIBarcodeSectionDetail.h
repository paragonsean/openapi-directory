/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIBarcodeSectionDetail.h
 *
 * 
 */

#ifndef OAIBarcodeSectionDetail_H
#define OAIBarcodeSectionDetail_H

#include <QJsonObject>

#include "OAIFieldSelector.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIFieldSelector;

class OAIBarcodeSectionDetail : public OAIObject {
public:
    OAIBarcodeSectionDetail();
    OAIBarcodeSectionDetail(QString json);
    ~OAIBarcodeSectionDetail() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIFieldSelector getFieldSelector() const;
    void setFieldSelector(const OAIFieldSelector &field_selector);
    bool is_field_selector_Set() const;
    bool is_field_selector_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIFieldSelector m_field_selector;
    bool m_field_selector_isSet;
    bool m_field_selector_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBarcodeSectionDetail)

#endif // OAIBarcodeSectionDetail_H
