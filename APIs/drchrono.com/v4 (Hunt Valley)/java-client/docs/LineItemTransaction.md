

# LineItemTransaction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adjustment** | **BigDecimal** | Adjustment from total billed |  [optional] |
|**adjustmentGroupCode** | [**AdjustmentGroupCodeEnum**](#AdjustmentGroupCodeEnum) | Group code for adjustment |  [optional] [readonly] |
|**adjustmentReason** | [**AdjustmentReasonEnum**](#AdjustmentReasonEnum) | Reason for adjustment |  [optional] |
|**appointment** | **Integer** | Appointment ID |  [optional] |
|**checkDate** | **String** | Date of check |  [optional] [readonly] |
|**claimStatus** | [**ClaimStatusEnum**](#ClaimStatusEnum) | Status of claim |  [optional] [readonly] |
|**createdAt** | **String** |  |  [optional] [readonly] |
|**doctor** | **Integer** | Doctor ID |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**insName** | **Integer** | Can be one of the following, &#x60;1&#x60;(Primary Insurance), &#x60;2&#x60;(Secondary Insurance) |  [optional] |
|**insPaid** | **BigDecimal** |  |  [optional] |
|**lineItem** | **Integer** | ID of &#x60;/api/line_item&#x60; object |  [optional] |
|**patient** | **Integer** |  |  [optional] |
|**postedDate** | **String** | Date when transaction is created |  [optional] [readonly] |
|**traceNumber** | **String** | Check number |  [optional] |
|**updatedAt** | **String** |  |  [optional] [readonly] |



## Enum: AdjustmentGroupCodeEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| CO | &quot;CO&quot; |
| OA | &quot;OA&quot; |
| PI | &quot;PI&quot; |
| PR | &quot;PR&quot; |



## Enum: AdjustmentReasonEnum

| Name | Value |
|---- | -----|
| _3 | &quot;-3&quot; |
| _2 | &quot;-2&quot; |
| _4 | &quot;-4&quot; |
| _1 | &quot;-1&quot; |
| _0 | &quot;0&quot; |
| _12 | &quot;1&quot; |
| _22 | &quot;2&quot; |
| _32 | &quot;3&quot; |
| _42 | &quot;4&quot; |
| _5 | &quot;5&quot; |
| _6 | &quot;6&quot; |
| _7 | &quot;7&quot; |
| _8 | &quot;8&quot; |
| _9 | &quot;9&quot; |
| _10 | &quot;10&quot; |
| _11 | &quot;11&quot; |
| _12 | &quot;12&quot; |
| _13 | &quot;13&quot; |
| _14 | &quot;14&quot; |
| _15 | &quot;15&quot; |
| _16 | &quot;16&quot; |
| _18 | &quot;18&quot; |
| _19 | &quot;19&quot; |
| _20 | &quot;20&quot; |
| _21 | &quot;21&quot; |
| _22 | &quot;22&quot; |
| _23 | &quot;23&quot; |
| _24 | &quot;24&quot; |
| _26 | &quot;26&quot; |
| _27 | &quot;27&quot; |
| _29 | &quot;29&quot; |
| _31 | &quot;31&quot; |
| _32 | &quot;32&quot; |
| _33 | &quot;33&quot; |
| _34 | &quot;34&quot; |
| _35 | &quot;35&quot; |
| _39 | &quot;39&quot; |
| _40 | &quot;40&quot; |
| _44 | &quot;44&quot; |
| _45 | &quot;45&quot; |
| _49 | &quot;49&quot; |
| _50 | &quot;50&quot; |
| _51 | &quot;51&quot; |
| _53 | &quot;53&quot; |
| _54 | &quot;54&quot; |
| _55 | &quot;55&quot; |
| _56 | &quot;56&quot; |
| _58 | &quot;58&quot; |
| _59 | &quot;59&quot; |
| _60 | &quot;60&quot; |
| _61 | &quot;61&quot; |
| _66 | &quot;66&quot; |
| _69 | &quot;69&quot; |
| _70 | &quot;70&quot; |
| _74 | &quot;74&quot; |
| _75 | &quot;75&quot; |
| _76 | &quot;76&quot; |
| _78 | &quot;78&quot; |
| _85 | &quot;85&quot; |
| _87 | &quot;87&quot; |
| _89 | &quot;89&quot; |
| _90 | &quot;90&quot; |
| _91 | &quot;91&quot; |
| _94 | &quot;94&quot; |
| _95 | &quot;95&quot; |
| _96 | &quot;96&quot; |
| _97 | &quot;97&quot; |
| _100 | &quot;100&quot; |
| _101 | &quot;101&quot; |
| _102 | &quot;102&quot; |
| _103 | &quot;103&quot; |
| _104 | &quot;104&quot; |
| _105 | &quot;105&quot; |
| _106 | &quot;106&quot; |
| _107 | &quot;107&quot; |
| _108 | &quot;108&quot; |
| _109 | &quot;109&quot; |
| _110 | &quot;110&quot; |
| _111 | &quot;111&quot; |
| _112 | &quot;112&quot; |
| _114 | &quot;114&quot; |
| _115 | &quot;115&quot; |
| _116 | &quot;116&quot; |
| _117 | &quot;117&quot; |
| _118 | &quot;118&quot; |
| _119 | &quot;119&quot; |
| _121 | &quot;121&quot; |
| _122 | &quot;122&quot; |
| _125 | &quot;125&quot; |
| _128 | &quot;128&quot; |
| _129 | &quot;129&quot; |
| _130 | &quot;130&quot; |
| _131 | &quot;131&quot; |
| _132 | &quot;132&quot; |
| _133 | &quot;133&quot; |
| _134 | &quot;134&quot; |
| _135 | &quot;135&quot; |
| _136 | &quot;136&quot; |
| _137 | &quot;137&quot; |
| _138 | &quot;138&quot; |
| _139 | &quot;139&quot; |
| _140 | &quot;140&quot; |
| _142 | &quot;142&quot; |
| _143 | &quot;143&quot; |
| _144 | &quot;144&quot; |
| _146 | &quot;146&quot; |
| _147 | &quot;147&quot; |
| _148 | &quot;148&quot; |
| _149 | &quot;149&quot; |
| _150 | &quot;150&quot; |
| _151 | &quot;151&quot; |
| _152 | &quot;152&quot; |
| _153 | &quot;153&quot; |
| _154 | &quot;154&quot; |
| _155 | &quot;155&quot; |
| _157 | &quot;157&quot; |
| _158 | &quot;158&quot; |
| _159 | &quot;159&quot; |
| _160 | &quot;160&quot; |
| _161 | &quot;161&quot; |
| _162 | &quot;162&quot; |
| _163 | &quot;163&quot; |
| _164 | &quot;164&quot; |
| _165 | &quot;165&quot; |
| _166 | &quot;166&quot; |
| _167 | &quot;167&quot; |
| _168 | &quot;168&quot; |
| _169 | &quot;169&quot; |
| _170 | &quot;170&quot; |
| _171 | &quot;171&quot; |
| _172 | &quot;172&quot; |
| _173 | &quot;173&quot; |
| _174 | &quot;174&quot; |
| _175 | &quot;175&quot; |
| _176 | &quot;176&quot; |
| _177 | &quot;177&quot; |
| _178 | &quot;178&quot; |
| _179 | &quot;179&quot; |
| _180 | &quot;180&quot; |
| _181 | &quot;181&quot; |
| _182 | &quot;182&quot; |
| _183 | &quot;183&quot; |
| _184 | &quot;184&quot; |
| _185 | &quot;185&quot; |
| _186 | &quot;186&quot; |
| _187 | &quot;187&quot; |
| _188 | &quot;188&quot; |
| _189 | &quot;189&quot; |
| _190 | &quot;190&quot; |
| _191 | &quot;191&quot; |
| _192 | &quot;192&quot; |
| _193 | &quot;193&quot; |
| _194 | &quot;194&quot; |
| _195 | &quot;195&quot; |
| _197 | &quot;197&quot; |
| _198 | &quot;198&quot; |
| _199 | &quot;199&quot; |
| _200 | &quot;200&quot; |
| _201 | &quot;201&quot; |
| _202 | &quot;202&quot; |
| _203 | &quot;203&quot; |
| _204 | &quot;204&quot; |
| _205 | &quot;205&quot; |
| _206 | &quot;206&quot; |
| _207 | &quot;207&quot; |
| _208 | &quot;208&quot; |
| _209 | &quot;209&quot; |
| _210 | &quot;210&quot; |
| _211 | &quot;211&quot; |
| _212 | &quot;212&quot; |
| _213 | &quot;213&quot; |
| _214 | &quot;214&quot; |
| _215 | &quot;215&quot; |
| _216 | &quot;216&quot; |
| _217 | &quot;217&quot; |
| _218 | &quot;218&quot; |
| _219 | &quot;219&quot; |
| _220 | &quot;220&quot; |
| _221 | &quot;221&quot; |
| _222 | &quot;222&quot; |
| _223 | &quot;223&quot; |
| _224 | &quot;224&quot; |
| _225 | &quot;225&quot; |
| _226 | &quot;226&quot; |
| _227 | &quot;227&quot; |
| _228 | &quot;228&quot; |
| _229 | &quot;229&quot; |
| _230 | &quot;230&quot; |
| _231 | &quot;231&quot; |
| _232 | &quot;232&quot; |
| _233 | &quot;233&quot; |
| _234 | &quot;234&quot; |
| _235 | &quot;235&quot; |
| _236 | &quot;236&quot; |
| _237 | &quot;237&quot; |
| _238 | &quot;238&quot; |
| _239 | &quot;239&quot; |
| _240 | &quot;240&quot; |
| _241 | &quot;241&quot; |
| _242 | &quot;242&quot; |
| _243 | &quot;243&quot; |
| _244 | &quot;244&quot; |
| _245 | &quot;245&quot; |
| _246 | &quot;246&quot; |
| _247 | &quot;247&quot; |
| _248 | &quot;248&quot; |
| _249 | &quot;249&quot; |
| _250 | &quot;250&quot; |
| _251 | &quot;251&quot; |
| _252 | &quot;252&quot; |
| _253 | &quot;253&quot; |
| _254 | &quot;254&quot; |
| _256 | &quot;256&quot; |
| _257 | &quot;257&quot; |
| _258 | &quot;258&quot; |
| _259 | &quot;259&quot; |
| _260 | &quot;260&quot; |
| _261 | &quot;261&quot; |
| _262 | &quot;262&quot; |
| _263 | &quot;263&quot; |
| _264 | &quot;264&quot; |
| _265 | &quot;265&quot; |
| _266 | &quot;266&quot; |
| _267 | &quot;267&quot; |
| _268 | &quot;268&quot; |
| _269 | &quot;269&quot; |
| _270 | &quot;270&quot; |
| _271 | &quot;271&quot; |
| _272 | &quot;272&quot; |
| _273 | &quot;273&quot; |
| _274 | &quot;274&quot; |
| _275 | &quot;275&quot; |
| _276 | &quot;276&quot; |
| _277 | &quot;277&quot; |
| _287 | &quot;287&quot; |
| _288 | &quot;288&quot; |
| A0 | &quot;A0&quot; |
| A1 | &quot;A1&quot; |
| A5 | &quot;A5&quot; |
| A6 | &quot;A6&quot; |
| A7 | &quot;A7&quot; |
| A8 | &quot;A8&quot; |
| B1 | &quot;B1&quot; |
| B4 | &quot;B4&quot; |
| B5 | &quot;B5&quot; |
| B7 | &quot;B7&quot; |
| B8 | &quot;B8&quot; |
| B9 | &quot;B9&quot; |
| B10 | &quot;B10&quot; |
| B11 | &quot;B11&quot; |
| B12 | &quot;B12&quot; |
| B13 | &quot;B13&quot; |
| B14 | &quot;B14&quot; |
| B15 | &quot;B15&quot; |
| B16 | &quot;B16&quot; |
| B20 | &quot;B20&quot; |
| B22 | &quot;B22&quot; |
| B23 | &quot;B23&quot; |
| P1 | &quot;P1&quot; |
| P2 | &quot;P2&quot; |
| P3 | &quot;P3&quot; |
| P4 | &quot;P4&quot; |
| P5 | &quot;P5&quot; |
| P6 | &quot;P6&quot; |
| P7 | &quot;P7&quot; |
| P8 | &quot;P8&quot; |
| P9 | &quot;P9&quot; |
| P10 | &quot;P10&quot; |
| P11 | &quot;P11&quot; |
| P12 | &quot;P12&quot; |
| P13 | &quot;P13&quot; |
| P14 | &quot;P14&quot; |
| P15 | &quot;P15&quot; |
| P16 | &quot;P16&quot; |
| P17 | &quot;P17&quot; |
| P18 | &quot;P18&quot; |
| P19 | &quot;P19&quot; |
| P20 | &quot;P20&quot; |
| P21 | &quot;P21&quot; |
| P22 | &quot;P22&quot; |
| P23 | &quot;P23&quot; |
| W1 | &quot;W1&quot; |
| W2 | &quot;W2&quot; |
| W3 | &quot;W3&quot; |
| W4 | &quot;W4&quot; |
| Y1 | &quot;Y1&quot; |
| Y2 | &quot;Y2&quot; |
| Y3 | &quot;Y3&quot; |



## Enum: ClaimStatusEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| _0 | &quot;0&quot; |
| _1 | &quot;1&quot; |
| _2 | &quot;2&quot; |
| _3 | &quot;3&quot; |
| _4 | &quot;4&quot; |
| _5 | &quot;5&quot; |
| _10 | &quot;10&quot; |
| _13 | &quot;13&quot; |
| _15 | &quot;15&quot; |
| _16 | &quot;16&quot; |
| _17 | &quot;17&quot; |
| _19 | &quot;19&quot; |
| _20 | &quot;20&quot; |
| _21 | &quot;21&quot; |
| _22 | &quot;22&quot; |
| _23 | &quot;23&quot; |
| _25 | &quot;25&quot; |
| _27 | &quot;27&quot; |



