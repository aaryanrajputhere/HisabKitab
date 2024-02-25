//
//  HomeView.swift
//  SPLITWISE
//
//  Created by Irfan on 23/02/24.
//

import SwiftUI

struct HomeView: View {
    
    var body: some View {
        ZStack{
            Color.color.ignoresSafeArea()
            
            ScrollView{
                
                VStack{
                    
                    ZStack{
                        Rectangle().frame(width:380,height:240).cornerRadius(20).padding(.top,15)
                        
                        VStack{
                            
                            HStack{
                                Image(systemName:"function").foregroundColor(.white).font(.system(size: 40))
                                
                                Text("HisabKitab").fontWeight(.heavy).foregroundColor(.neon).font(.system(size: 40))
                                
                            }.padding(.top,19)
                            
                            Rectangle().size(width: 350, height: 2).foregroundColor(.gray)
                            
                            Text("Dashboard").fontWeight(.bold).foregroundColor(.white).frame(width:340,alignment: .leading).font(.system(size: 30))
                            
                            HStack{
                                ZStack{
                                    Rectangle().frame(width:110,height:65).foregroundColor(.color).cornerRadius(10)
                                    VStack{
                                        Text("BALANCE").foregroundColor(.white).fontWeight(.semibold).font(.system(size:20))
                                        HStack{
                                            Image(systemName: "indianrupeesign").foregroundColor(.green)
                                           Text("1500").foregroundColor(.green).font(.system(size:24))
                                        }
                                        
                                    }
                                }
                                
                                ZStack{
                                    Rectangle().frame(width:110,height:65).foregroundColor(.color).cornerRadius(10)
                                    VStack{
                                        Text("OWE").foregroundColor(.white).fontWeight(.semibold).font(.system(size:20))
                                        HStack{
                                            Image(systemName: "indianrupeesign").foregroundColor(.red)
                                            Text("900").foregroundColor(.red).font(.system(size:24))
                                        }
                                        
                                    }

                                }
                                
                                ZStack{
                                    Rectangle().frame(width:110,height:65).foregroundColor(.color).cornerRadius(10)
                                    VStack{
                                        Text("OWED").foregroundColor(.white).fontWeight(.semibold).font(.system(size:18))
                                        HStack{
                                            Image(systemName: "indianrupeesign").foregroundColor(.green)
                                            Text("1500").foregroundColor(.green).font(.system(size:24))
                                            
                                        }
                                        
                                    }

                                }
                                
                                
                                
                                
                            }
                            
                        }.frame(width:340,height:230,alignment: .leading).padding(.bottom,10)
                        
                    }
                    
                    
                    
                    ScrollView(.horizontal){
                        
                        HStack(spacing:8){
                            
                            
                            Image(.image).resizable().frame(width: 230, height: 200).cornerRadius(20)
                            Image(.image1).resizable().frame(width: 230, height: 200).cornerRadius(20)

                            Image(.image2).resizable().frame(width: 250, height: 200).cornerRadius(20)

                            Image(.image3).resizable().frame(width: 230, height: 200).cornerRadius(20)

                            
                        }
                        
                    }.padding([.top,.leading,.trailing],10)
                    
                    ZStack{
                        Rectangle().frame(width:375,height:200).cornerRadius(10)
                        
                        //Progress of Social Score
                        
                    }.padding(.top,10)
                
                
                
            }
        
                Spacer()
                
            }
            
            
        }
        
    }
}

#Preview {
    HomeView()
}
