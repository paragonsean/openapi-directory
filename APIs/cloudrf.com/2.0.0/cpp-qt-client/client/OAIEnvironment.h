/**
 * Cloud-RF API
 * Use this JSON API to build and test radio links for any radio, anywhere. Authenticate with your API2.0 key in the request header as key
 *
 * The version of the OpenAPI document: 2.0.0
 * Contact: support@cloudrf.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIEnvironment.h
 *
 * 
 */

#ifndef OAIEnvironment_H
#define OAIEnvironment_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIEnvironment : public OAIObject {
public:
    OAIEnvironment();
    OAIEnvironment(QString json);
    ~OAIEnvironment() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getCll() const;
    void setCll(const qint32 &cll);
    bool is_cll_Set() const;
    bool is_cll_Valid() const;

    qint32 getClm() const;
    void setClm(const qint32 &clm);
    bool is_clm_Set() const;
    bool is_clm_Valid() const;

    float getMat() const;
    void setMat(const float &mat);
    bool is_mat_Set() const;
    bool is_mat_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_cll;
    bool m_cll_isSet;
    bool m_cll_isValid;

    qint32 m_clm;
    bool m_clm_isSet;
    bool m_clm_isValid;

    float m_mat;
    bool m_mat_isSet;
    bool m_mat_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEnvironment)

#endif // OAIEnvironment_H
