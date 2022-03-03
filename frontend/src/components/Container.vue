<template>
  <div class="row">
  <div class="col-lg-6">
    <input type="text" v-model="name" class="form-control mt-2" placeholder="Name">
    <input type="text" v-model="email" class="form-control mt-2" placeholder="Email">
    <input type="text" v-model="phone" class="form-control mt-2" placeholder="Phone">
    <button @click="postOne" class="btn btn-block btn-success">Update</button>
  </div>
  <div class="col-lg-6">
    <table class="table">
      <thead>
        <th>Id</th>
        <th>Name</th>
        <th>Email</th>
        <th>Phone</th>
        <th>Edit</th>
        <th>Delete</th>
      </thead>
      <tbody>
        <tr v-for="contact in contacts" v-bind:key="contact.id">
          <td>{{contact.id}}</td>
          <td>{{contact.name}}</td>
          <td>{{contact.email}}</td>
          <td>{{contact.phone}}</td>
          <td>
            <button @click="getOne(contact)" class="btn bn-sm btn-success"><i class="fa-solid fa-pencil"></i></button>
          </td>
          <td>
            <button @click="deleteOne(contact.id)" class="btn bn-sm btn-success"><i class="fa-solid fa-trash"></i></button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Contact-Container',
  props: {
    msg: String
  },
  data(){
    return{
      contacts: null,
      name: '',
      email: '',
      phone: ''
    }
  },
  mounted(){
    this.getAll();
  },
  methods:{
    getAll(){
      axios.get('http://localhost:8000/contacts/')
      .then((res)=>{
        this.contacts=res.data
      })
    },
    getOne(contact){
      this.id = contact.id;
      this.name = contact.name;
      this.email = contact.email;
      this.phone = contact.phone;
    },
    deleteOne(id){
      axios.delete(`http://localhost:8000/contacts/${id}`)
    },
    updateOne(){
      axios.post('http://localhost:8000/contacts/'),
      {name:this.name, email:this.email, phone:this.phone}
    }
  }
}
</script>

<style scoped>

</style>
