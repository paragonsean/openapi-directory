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
 * OAIMixins.h
 *
 * 
 */

#ifndef OAIMixins_H
#define OAIMixins_H

#include <QJsonObject>

#include "OAIMixin.h"
#include "OAIUnstable_mixins.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIMixin;
class OAIUnstable_mixins;

class OAIMixins : public OAIObject {
public:
    OAIMixins();
    OAIMixins(QString json);
    ~OAIMixins() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIMixin> getMixin() const;
    void setMixin(const QList<OAIMixin> &mixin);
    bool is_mixin_Set() const;
    bool is_mixin_Valid() const;

    OAIUnstable_mixins getUnstableMixins() const;
    void setUnstableMixins(const OAIUnstable_mixins &unstable_mixins);
    bool is_unstable_mixins_Set() const;
    bool is_unstable_mixins_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIMixin> m_mixin;
    bool m_mixin_isSet;
    bool m_mixin_isValid;

    OAIUnstable_mixins m_unstable_mixins;
    bool m_unstable_mixins_isSet;
    bool m_unstable_mixins_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIMixins)

#endif // OAIMixins_H
