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
 * OAICardTemplateOverride.h
 *
 * 
 */

#ifndef OAICardTemplateOverride_H
#define OAICardTemplateOverride_H

#include <QJsonObject>

#include "OAICardRowTemplateInfo.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICardRowTemplateInfo;

class OAICardTemplateOverride : public OAIObject {
public:
    OAICardTemplateOverride();
    OAICardTemplateOverride(QString json);
    ~OAICardTemplateOverride() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAICardRowTemplateInfo> getCardRowTemplateInfos() const;
    void setCardRowTemplateInfos(const QList<OAICardRowTemplateInfo> &card_row_template_infos);
    bool is_card_row_template_infos_Set() const;
    bool is_card_row_template_infos_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAICardRowTemplateInfo> m_card_row_template_infos;
    bool m_card_row_template_infos_isSet;
    bool m_card_row_template_infos_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICardTemplateOverride)

#endif // OAICardTemplateOverride_H
