/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIContributions_mixin_contributor_contributor_contributor.h
 *
 * 
 */

#ifndef OAIContributions_mixin_contributor_contributor_contributor_H
#define OAIContributions_mixin_contributor_contributor_contributor_H

#include <QJsonObject>

#include "OAIContributions_mixin_contributor_name.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIContributions_mixin_contributor_name;

class OAIContributions_mixin_contributor_contributor_contributor : public OAIObject {
public:
    OAIContributions_mixin_contributor_contributor_contributor();
    OAIContributions_mixin_contributor_contributor_contributor(QString json);
    ~OAIContributions_mixin_contributor_contributor_contributor() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIContributions_mixin_contributor_name getContributionsMixinContributorName() const;
    void setContributionsMixinContributorName(const OAIContributions_mixin_contributor_name &contributions_mixin_contributor_name);
    bool is_contributions_mixin_contributor_name_Set() const;
    bool is_contributions_mixin_contributor_name_Valid() const;

    QString getHref() const;
    void setHref(const QString &href);
    bool is_href_Set() const;
    bool is_href_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIContributions_mixin_contributor_name m_contributions_mixin_contributor_name;
    bool m_contributions_mixin_contributor_name_isSet;
    bool m_contributions_mixin_contributor_name_isValid;

    QString m_href;
    bool m_href_isSet;
    bool m_href_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIContributions_mixin_contributor_contributor_contributor)

#endif // OAIContributions_mixin_contributor_contributor_contributor_H
