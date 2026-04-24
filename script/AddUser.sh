while IFS=, read -r username password; do
    [ -z "$username" ] && continue
    username=$(echo "$username" | xargs)
    password=$(echo "$password" | xargs)
    echo "正在處理使用者: $username"
    cmsAddUser "$username" "$username" "$username" -p "$password";
    cmsAddParticipation -c 1 "$username"

done <<EOF

S01,tsqpmd5p99
S02,kkciy9nx4f
S03,g3rgapug7v
S04,eda2qb4bby
S05,3cbu5jvp2c
S06,wzev6sqaj4
S07,5ixnacc2w2
S08,27yuaq2veg
S09,jach44ruva
S10,iv8tu2a8pv
S11,av4edahdgz
S12,yg8ix4zk9v
S13,p2vp9gfq3r
S14,5enuk36nxz
S15,32qws3erd2
S16,m6ysgdmt92
S17,7pwp29a4xj
S18,wbq75w6wfj
S19,j76qwahhz8
S20,jc47xmcbz2
S21,x2gjq9wv5d
S22,n26jc4c4u5
S23,22dk8bbuhi
S24,7xky34gfek
S25,6zszub2a4y
S26,i6idkjvw26
S27,6nrc2aa6ck
S28,r2e99cbjgz
S29,7z23s6neqj
S30,dzvrq6923b
S31,y2w59xqg4d
S32,hw59sk44is
S33,euu259rh5k
S34,jt6jkt52g7
S35,nxb39h5ngi
S36,auw78i5zmy
S37,ghbwr333ze
S38,ait5v5qfp7
S39,y6xa8mkp3z
S40,25vxeagz7e
S41,wsk3myd2q3
S42,rq6wqej5c2
S43,3fct3n6vjf
S44,k5bpk6e7fw
S45,tf5n8qyyw9
S46,gs7nhi4wf3
S47,m45d5gdcci
S48,8ahapy5ii4
S49,wp98emi3qm
S50,aaf7c1q6t9
S51,xaf4c5q8t6
S52,yaf2k2q6t3
S53,baf1c5q7t2
S54,zxf8g9q6t5
S55,rdf9c5q8t8
S56,hyf7d5q6t7
S57,jyf3c5q9t1
S58,rff6m3q6t2
S59,edf9c5q5t4
S60,wsf7c5q4t3
S61,ndf4c5q8t6
S62,cvf2k2q6t3
S63,rsf1c5q7t2
S64,gbf8g9q6t5
S65,gbf9c5q8t8
S66,cxf7d5q6t7
S67,kvf3c5q9tK
S68,cdf6m3q6t2
S69,rtf9c5q5t4
S70,nbf7c5q4t3
S71,sbf8c5q4t5
S72,tbf7c6q4t8
S73,bdf7s5q4t9
S74,ybf7d8q4t3
S75,nbf7c5q6p3
S76,hx9d2kpw5m
S77,3vnr8bqc7x
S78,yj4ft6a2es
S79,9qg5z1mxkp
S80,cu8w3rd7ny
S81,2kfa9hvj4t
S82,p5xb6q3zmd
S83,7ec2ns8r1g
S84,m3t9yw4vkb
S85,f8p1dz6jc5
S86,4nh7gq2xmr
S87,a6vw3k5yfb
S88,r1sz9c4pd8
S89,xk5b8tj2mn
S90,5jd7m3f9wq

EOF

